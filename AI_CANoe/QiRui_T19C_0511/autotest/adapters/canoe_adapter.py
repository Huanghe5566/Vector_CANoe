from __future__ import annotations

# 这个文件是 Python 和 CANoe 之间的“翻译员”。
# 测试用例不直接操作 CANoe COM 接口，而是调用这里的简单函数：
# - open_project() 打开 CANoe 工程
# - start_measurement() 启动 Measurement
# - set_signal() 设置信号
# - get_signal() 读取信号
#
# dry_run=True 表示“离线假跑”：
# - 不启动 CANoe
# - 信号值存在 Python 字典里
# - 方便没有台架时先测试 Python 框架逻辑

import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from autotest.core.config import ProjectConfig, SignalRef
from autotest.core.exceptions import CanoeError


@dataclass
class CanoeAdapter:
    """CANoe automation facade.

    dry_run=True is the default so framework tests can run without CANoe.
    Set dry_run=False only on a bench PC with CANoe and pywin32 installed.
    """

    config: ProjectConfig
    # dry_run=True：离线模式，不连 CANoe。
    # dry_run=False：真实模式，使用 pywin32 调 CANoe COM。
    dry_run: bool = True
    # visible=True：真实启动 CANoe 时显示窗口，便于人工观察。
    visible: bool = True
    # app 保存 CANoe.Application COM 对象。离线模式下保持 None。
    app: Any | None = None
    # signal_values / sysvar_values 是离线模式的“假 CANoe 内存”。
    signal_values: dict[str, Any] = field(default_factory=dict)
    sysvar_values: dict[str, Any] = field(default_factory=dict)
    # operation_log 记录离线模式下调用过哪些操作，便于单元测试检查。
    operation_log: list[tuple[str, Any]] = field(default_factory=list)

    def open_project(self) -> None:
        # 先从 YAML 配置里拿到 CANoe cfg 路径。
        cfg_path = self.config.canoe_cfg_path()
        if not cfg_path.exists():
            raise CanoeError(f"CANoe cfg does not exist: {cfg_path}")
        if self.dry_run:
            # 离线模式只记录“本来要打开这个工程”，不真的打开 CANoe。
            self.operation_log.append(("open_project", str(cfg_path)))
            return
        # 真实模式：启动 CANoe COM 服务，并打开 cfg。
        self.app = self._dispatch_canoe()
        self.app.Visible = self.visible
        # 不同 CANoe 版本暴露 Open 的位置可能略有差异，这里兼容两种写法。
        if hasattr(self.app, "Open"):
            self.app.Open(str(cfg_path))
        else:
            self.app.Configuration.Open(str(cfg_path))

    def start_measurement(self, timeout_s: float = 30.0) -> None:
        # Measurement 可以理解为 CANoe 的“开始运行”按钮。
        if self.dry_run:
            self.operation_log.append(("start_measurement", timeout_s))
            return
        self._require_app()
        self.app.Measurement.Start()
        self._wait_measurement_state(True, timeout_s)

    def stop_measurement(self, timeout_s: float = 10.0) -> None:
        # 停止 CANoe Measurement。真实台架测试结束后必须调用，避免总线继续发送。
        if self.dry_run:
            self.operation_log.append(("stop_measurement", timeout_s))
            return
        self._require_app()
        if self.app.Measurement.Running:
            self.app.Measurement.Stop()
            self._wait_measurement_state(False, timeout_s)

    def set_signal(self, ref: SignalRef, value: Any) -> None:
        # 设置信号值。
        # 如果 ref.sysvar 有值，说明这不是普通 CAN 信号，而是 CANoe 系统变量。
        if ref.sysvar:
            self.set_sysvar(ref.sysvar, value)
            return
        if self.dry_run:
            # 离线模式：把值存在字典里，模拟 CANoe 已经设置成功。
            self.signal_values[ref.key] = value
            self.operation_log.append(("set_signal", ref.key, value))
            return
        # 真实模式：通过 CANoe COM 找到信号对象，然后写 Value。
        signal = self._get_canoe_signal(ref)
        signal.Value = value

    def get_signal(self, ref: SignalRef) -> Any:
        # 读取信号值，逻辑和 set_signal 类似。
        if ref.sysvar:
            return self.get_sysvar(ref.sysvar)
        if self.dry_run:
            # 如果离线模式还没有设置过这个信号，默认返回 0。
            return self.signal_values.get(ref.key, 0)
        return self._get_canoe_signal(ref).Value

    def set_sysvar(self, sysvar: str, value: Any) -> None:
        # 设置 CANoe 系统变量。
        # 系统变量常用于面板按钮、故障注入开关、UDP 控制按钮等。
        if self.dry_run:
            self.sysvar_values[sysvar] = value
            self.operation_log.append(("set_sysvar", sysvar, value))
            return
        variable = self._get_system_variable(sysvar)
        variable.Value = value

    def get_sysvar(self, sysvar: str) -> Any:
        # 读取 CANoe 系统变量。
        if self.dry_run:
            return self.sysvar_values.get(sysvar, 0)
        return self._get_system_variable(sysvar).Value

    def close(self) -> None:
        # 统一关闭入口。真实模式下会先停 Measurement。
        if self.dry_run:
            self.operation_log.append(("close", None))
            return
        if self.app is not None:
            self.stop_measurement()
            self.app = None

    def _dispatch_canoe(self) -> Any:
        # pywin32 是 Python 调 Windows COM 的库。
        # CANoe 安装后会注册 "CANoe.Application" 这个 COM 名字。
        try:
            import win32com.client  # type: ignore
        except ImportError as exc:
            raise CanoeError("pywin32 is required for real CANoe automation.") from exc
        try:
            return win32com.client.Dispatch("CANoe.Application")
        except Exception as exc:  # pragma: no cover - depends on CANoe install
            raise CanoeError("Failed to start CANoe COM server.") from exc

    def _require_app(self) -> None:
        # 防止还没 open_project() 就调用 start/set/get。
        if self.app is None:
            raise CanoeError("CANoe project is not opened. Call open_project() first.")

    def _wait_measurement_state(self, running: bool, timeout_s: float) -> None:
        # 等待 CANoe Measurement 真的变成运行/停止状态。
        # 不能刚点 Start 就马上发 UDP，否则 CANoe 可能还没准备好。
        deadline = time.perf_counter() + timeout_s
        while time.perf_counter() < deadline:
            if bool(self.app.Measurement.Running) is running:
                return
            time.sleep(0.1)
        expected = "running" if running else "stopped"
        raise CanoeError(f"CANoe measurement did not become {expected} within {timeout_s}s.")

    def _get_canoe_signal(self, ref: SignalRef) -> Any:
        # 把 YAML 里的 network/message/signal 转成 CANoe COM 信号对象。
        self._require_app()
        if not ref.network or not ref.message or not ref.signal:
            raise CanoeError(f"Signal reference is incomplete: {ref}")
        bus_name = self._bus_name(ref.network)
        channel = ref.channel or self._channel_from_network(ref.network)
        try:
            # 例：network="CAN1" -> bus_name="CAN", channel=1。
            bus = self.app.GetBus(bus_name)
            return bus.GetSignal(channel, ref.message, ref.signal)
        except Exception as exc:  # pragma: no cover - depends on CANoe project API
            raise CanoeError(
                "Failed to access CANoe signal. Check network/channel/message/signal "
                f"mapping for {ref.logical_name}: {ref.key}"
            ) from exc

    def _get_system_variable(self, sysvar: str) -> Any:
        # 系统变量路径示例：
        # "UDP::UdpOpen" 或 "Vehicle_input::MSG::ACU_2_0x31"
        # CANoe COM 需要一层层进入 namespace，最后拿 variable。
        self._require_app()
        parts = [part for part in sysvar.split("::") if part]
        if len(parts) < 2:
            raise CanoeError(f"Invalid sysvar path: {sysvar}")
        try:
            namespace = self.app.System.Namespaces(parts[0])
            for name in parts[1:-1]:
                namespace = namespace.Namespaces(name)
            return namespace.Variables(parts[-1])
        except Exception as exc:  # pragma: no cover - depends on CANoe project API
            raise CanoeError(f"Failed to access CANoe sysvar: {sysvar}") from exc

    @staticmethod
    def _bus_name(network: str) -> str:
        # CANoe COM 里总线大类通常叫 CAN、Ethernet。
        # 配置里为了清楚会写 CAN1、CAN2，这里要转换一下。
        upper = network.upper()
        if upper.startswith("CAN"):
            return "CAN"
        if upper.startswith("ETH"):
            return "Ethernet"
        return network

    @staticmethod
    def _channel_from_network(network: str) -> int:
        # 从 "CAN1" 里提取数字 1，作为 CANoe 通道号。
        # 如果没有数字，就默认通道 1。
        digits = "".join(ch for ch in network if ch.isdigit())
        return int(digits) if digits else 1
