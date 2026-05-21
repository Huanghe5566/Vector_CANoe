from __future__ import annotations

# 这个文件负责车身信号。
# 用例层只写“设置车速 30”“档位 D”，不直接写 DBC 信号名。
# 真正的 DBC 信号名放在 project_config/t19c_rlcr_rrcr.yaml 里。

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.core.config import ProjectConfig


class VehicleService:
    def __init__(self, config: ProjectConfig, canoe: CanoeAdapter):
        self.config = config
        self.canoe = canoe

    def set_speed(self, speed_kph: float) -> None:
        # 设置车速。speed 这个逻辑名会在 YAML 中映射到真实 CAN 信号。
        self.canoe.set_signal(self.config.signal("speed"), speed_kph)

    def set_gear(self, gear_value: int | str) -> None:
        # 设置档位。
        # 用例可以写 "D"，也可以直接写数值 4。
        # 如果写 "D"，这里会从 YAML 的 vehicle_values.gear 找到 D=4。
        gear_map = self.config.section("vehicle_values").get("gear", {})
        value = gear_map.get(gear_value, gear_value)
        self.canoe.set_signal(self.config.signal("gear"), value)

    def set_switch(self, logical_name: str, enabled: bool) -> None:
        # 设置开关类信号，例如 BSD/LCA/RCTA 开关。
        # logical_name 是 YAML 中 vehicle_signals 下的名字。
        ref = self.config.signal(logical_name)
        signal_cfg = self.config.section("vehicle_signals").get(logical_name, {})
        values_key = signal_cfg.get("value_map", "switch")
        switch_values = self.config.section("vehicle_values").get(values_key, {})
        value = switch_values.get("on" if enabled else "off", 1 if enabled else 0)
        self.canoe.set_signal(ref, value)
