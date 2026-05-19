from __future__ import annotations

# 这个文件专门负责“读取配置”。
# 小白可以这样理解：
# - YAML 配置文件像一张表，里面写 CANoe 工程路径、信号名、UDP 地址等。
# - Python 用这个文件把 YAML 读进来。
# - 以后换项目时，尽量改 YAML，不改测试用例代码。

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .exceptions import ConfigError


@dataclass(frozen=True)
class SignalRef:
    """一个 CANoe 信号或系统变量的“地址”。

    例如车速信号可能在：
    CAN1 网络 -> ABS_ESP_1 报文 -> ABS_ESP_1_VehicleSpeedVSOSig 信号。

    logical_name 是我们自己给它起的简单名字，比如 speed。
    测试用例只写 speed，不直接写一长串 DBC 信号名。
    """

    logical_name: str
    network: str | None = None
    message: str | None = None
    signal: str | None = None
    node: str | None = None
    channel: int | None = None
    sysvar: str | None = None

    @classmethod
    def from_mapping(cls, logical_name: str, data: dict[str, Any]) -> "SignalRef":
        # YAML 里每个信号都必须是 key/value 形式。
        # 如果写成字符串或列表，就说明配置格式不对，直接报错。
        if not isinstance(data, dict):
            raise ConfigError(f"Signal '{logical_name}' must be a mapping.")
        return cls(
            logical_name=logical_name,
            network=data.get("network"),
            message=data.get("message"),
            signal=data.get("signal"),
            node=data.get("node"),
            channel=data.get("channel"),
            sysvar=data.get("sysvar"),
        )

    @property
    def key(self) -> str:
        # key 是 dry_run 离线测试时用的“字典键”。
        # 真实 CANoe 会直接访问信号，离线模式没有 CANoe，所以用这个字符串保存模拟值。
        if self.sysvar:
            return f"sysvar::{self.sysvar}"
        parts = [self.network or "", self.message or "", self.signal or ""]
        return "::".join(parts)


class ProjectConfig:
    """项目配置对象。

    它把 YAML 包装成更好用的 Python 对象。
    例如：
    - config.canoe_cfg_path() 取 CANoe 工程路径
    - config.signal("speed") 取车速信号映射
    - config.alarm_signal("rlcr_bsd_warn") 取报警输出信号映射
    """

    def __init__(self, path: Path, data: dict[str, Any]):
        self.path = path.resolve()
        self.data = data
        self.config_dir = self.path.parent
        # 当前配置文件一般在 autotest/project_config/xxx.yaml。
        # parents[2] 就是工程根目录 QiRui_T19C_0511。
        self.project_root = self.path.parents[2]

    @classmethod
    def load(cls, path: str | Path) -> "ProjectConfig":
        # 读取 YAML 文件。
        # encoding="utf-8" 是为了支持中文注释和中文路径。
        config_path = Path(path).resolve()
        if not config_path.exists():
            raise ConfigError(f"Config file does not exist: {config_path}")
        with config_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            raise ConfigError(f"Config root must be a mapping: {config_path}")
        return cls(config_path, data)

    def section(self, name: str) -> dict[str, Any]:
        # 读取一个配置章节，比如 project、udp_point_cloud、vehicle_signals。
        # 如果章节不存在，返回空字典，便于调用方自己决定是否允许为空。
        value = self.data.get(name, {})
        if not isinstance(value, dict):
            raise ConfigError(f"Section '{name}' must be a mapping.")
        return value

    def require_section(self, name: str) -> dict[str, Any]:
        # 和 section() 类似，但这个函数要求章节必须存在且非空。
        # 例如 project、udp_point_cloud 这种关键配置就应该用 require_section。
        value = self.section(name)
        if not value:
            raise ConfigError(f"Missing or empty section '{name}'.")
        return value

    def resolve_path(self, value: str | Path) -> Path:
        # 把 YAML 里的相对路径变成绝对路径。
        # 优先按“配置文件所在目录”解析；如果找不到，再按“工程根目录”解析。
        # 这样 YAML 写 "../../Chery_T19C.cfg" 或 "Chery_T19C.cfg" 都比较灵活。
        raw = Path(value)
        if raw.is_absolute():
            return raw
        from_config = (self.config_dir / raw).resolve()
        if from_config.exists():
            return from_config
        return (self.project_root / raw).resolve()

    def canoe_cfg_path(self) -> Path:
        # 返回 CANoe 工程 cfg 文件路径。
        # 如果 YAML 里没有 project.canoe_cfg，说明无法启动 CANoe，直接报错。
        project = self.require_section("project")
        cfg = project.get("canoe_cfg")
        if not cfg:
            raise ConfigError("project.canoe_cfg is required.")
        return self.resolve_path(cfg)

    def signal(self, logical_name: str, section: str = "vehicle_signals") -> SignalRef:
        # 根据简单名字查信号。
        # 例：config.signal("speed") -> CAN1::ABS_ESP_1::ABS_ESP_1_VehicleSpeedVSOSig
        signals = self.require_section(section)
        if logical_name not in signals:
            raise ConfigError(f"Unknown {section} signal: {logical_name}")
        return SignalRef.from_mapping(logical_name, signals[logical_name])

    def alarm(self, logical_name: str) -> dict[str, Any]:
        # 根据简单名字查报警配置。
        # 例：rlcr_bsd_warn 对应 RLCR_1_BSDWarn，active_values 表示哪些值算报警激活。
        alarms = self.require_section("alarm_outputs")
        if logical_name not in alarms:
            raise ConfigError(f"Unknown alarm output: {logical_name}")
        value = alarms[logical_name]
        if not isinstance(value, dict):
            raise ConfigError(f"Alarm '{logical_name}' must be a mapping.")
        return value

    def alarm_signal(self, logical_name: str) -> SignalRef:
        # 报警本质上也是一个 CAN 信号，所以复用 SignalRef。
        return SignalRef.from_mapping(logical_name, self.alarm(logical_name))

    def scenario_path(self, name_or_path: str | Path) -> Path:
        # 支持两种写法：
        # 1. "bsd_target_approach_left" -> 自动去 scenario_library 里找同名 yaml
        # 2. "xxx/yyy.yaml" -> 直接按路径读取
        raw = Path(name_or_path)
        if raw.suffix in {".yaml", ".yml"}:
            return self.resolve_path(raw)
        scenario_dir = self.section("paths").get("scenario_library", "../scenario_library")
        return self.resolve_path(Path(scenario_dir) / f"{raw}.yaml")


def load_yaml(path: str | Path) -> dict[str, Any]:
    # 通用 YAML 读取函数，场景文件也用它。
    file_path = Path(path).resolve()
    if not file_path.exists():
        raise ConfigError(f"YAML file does not exist: {file_path}")
    with file_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"YAML root must be a mapping: {file_path}")
    return data
