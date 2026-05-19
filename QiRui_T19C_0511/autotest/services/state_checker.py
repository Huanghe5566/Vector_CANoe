from __future__ import annotations

# 这个文件负责“状态机检查”。
# 状态机可以理解为雷达当前工作模式：
# init 初始化、standby 待机、active 工作、fault 故障。
# 状态值和名字的对应关系放在 YAML 的 state_machine.states 中。

import time

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.core.config import ProjectConfig, SignalRef
from autotest.core.exceptions import CheckError, ConfigError
from autotest.core.timing import monotonic_ms


class StateChecker:
    def __init__(self, config: ProjectConfig, canoe: CanoeAdapter):
        self.config = config
        self.canoe = canoe

    def state_signal(self) -> SignalRef:
        # 从 YAML 里读取状态机对应的 CAN 信号。
        state_machine = self.config.require_section("state_machine")
        mapping = state_machine.get("state_signal")
        if not isinstance(mapping, dict):
            raise ConfigError("state_machine.state_signal must be configured.")
        return SignalRef.from_mapping("radar_state", mapping)

    def read_state_value(self) -> object:
        # 读取状态信号的原始值，例如 0、1、2、3。
        return self.canoe.get_signal(self.state_signal())

    def read_state_name(self) -> str:
        # 把原始值翻译成人能看懂的名字。
        # 例：2 -> active。
        value = self.read_state_value()
        for name, configured_value in self.config.section("state_machine").get("states", {}).items():
            if value == configured_value or str(value) == str(configured_value):
                return name
        return f"unknown({value})"

    def wait_for_state(self, expected_state: str, timeout_ms: int, poll_ms: int = 10) -> bool:
        # 在 timeout_ms 时间内等待进入指定状态。
        # 成功返回 True，超时返回 False。
        states = self.config.section("state_machine").get("states", {})
        if expected_state not in states:
            raise CheckError(f"Unknown expected state: {expected_state}")
        deadline = monotonic_ms() + timeout_ms
        while monotonic_ms() <= deadline:
            if self.read_state_name() == expected_state:
                return True
            time.sleep(poll_ms / 1000.0)
        return False
