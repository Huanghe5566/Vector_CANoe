from __future__ import annotations

# 这个文件负责“场景”。
# 场景 YAML 里会写：
# - vehicle：车速、档位、开关
# - objects：点云目标
# - expected：期望报警
# 这个服务把这些内容翻译成实际动作。

from pathlib import Path
from typing import Any

from autotest.adapters.udp_replay_adapter import UdpReplayAdapter, UdpReplayStats
from autotest.core.config import ProjectConfig, load_yaml
from autotest.services.vehicle_service import VehicleService


class RadarSceneService:
    def __init__(self, config: ProjectConfig, vehicle: VehicleService, udp_replayer: UdpReplayAdapter):
        self.config = config
        self.vehicle = vehicle
        self.udp_replayer = udp_replayer

    def load(self, name_or_path: str | Path) -> dict[str, Any]:
        # 根据场景名读取 YAML。
        # 例：load("empty_scene") 会读取 autotest/scenario_library/empty_scene.yaml。
        return load_yaml(self.config.scenario_path(name_or_path))

    def apply_vehicle(self, scenario: dict[str, Any]) -> None:
        # 按场景里的 vehicle 字段设置车身条件。
        vehicle = scenario.get("vehicle", {})
        if "speed_kph" in vehicle:
            self.vehicle.set_speed(vehicle["speed_kph"])
        if "gear" in vehicle:
            self.vehicle.set_gear(vehicle["gear"])
        for key, value in vehicle.items():
            if key in {"speed_kph", "gear"}:
                continue
            # 除 speed_kph/gear 以外，其它 vehicle 字段先按开关处理。
            # 例如 bsd_lca_rcta_switch: true。
            self.vehicle.set_switch(key, bool(value))

    def play(self, name_or_scenario: str | Path | dict[str, Any], apply_vehicle: bool = True) -> UdpReplayStats:
        # 播放场景：
        # 1. 如果传入的是名字，就先加载 YAML。
        # 2. 根据 vehicle 设置车身条件。
        # 3. 根据 objects 发送 UDP 点云。
        scenario = self.load(name_or_scenario) if not isinstance(name_or_scenario, dict) else name_or_scenario
        if apply_vehicle:
            self.apply_vehicle(scenario)
        return self.udp_replayer.play_scenario(scenario)
