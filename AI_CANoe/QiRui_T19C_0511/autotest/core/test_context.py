from __future__ import annotations

# HilContext 是测试运行时的“工具箱”。
# pytest 用例里拿到 hil 后，就可以这样写：
# - hil.vehicle.set_speed(30)        设置车速
# - hil.radar_scene.play("xxx")      播放点云场景
# - hil.alarm.expect_active("xxx")   检查报警
# 这样用例不会直接碰 CANoe、socket、YAML 这些底层细节。

from dataclasses import dataclass

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.adapters.udp_replay_adapter import UdpReplayAdapter
from autotest.core.config import ProjectConfig
from autotest.services.alarm_checker import AlarmChecker
from autotest.services.evidence_collector import EvidenceCollector
from autotest.services.radar_scene import RadarSceneService
from autotest.services.state_checker import StateChecker
from autotest.services.vehicle_service import VehicleService


@dataclass
class HilContext:
    # 项目配置，来自 YAML。
    config: ProjectConfig
    # CANoe 控制器。
    canoe: CanoeAdapter
    # UDP 点云回灌器。
    udp_replayer: UdpReplayAdapter
    # 车身信号服务。
    vehicle: VehicleService
    # 场景服务：负责加载场景、设置车身条件、播放点云。
    radar_scene: RadarSceneService
    # 报警判定服务。
    alarm: AlarmChecker
    # 状态机判定服务。
    state: StateChecker
    # 证据收集服务，比如保存 JSON 日志。
    evidence: EvidenceCollector

    @classmethod
    def create(cls, config: ProjectConfig, dry_run: bool = True, canoe_visible: bool = True) -> "HilContext":
        # 这里统一创建所有服务对象。
        # 用例不需要自己 new CanoeAdapter 或 UdpReplayAdapter。
        canoe = CanoeAdapter(config=config, dry_run=dry_run, visible=canoe_visible)
        udp_replayer = UdpReplayAdapter.from_config(config.require_section("udp_point_cloud"))
        vehicle = VehicleService(config, canoe)
        return cls(
            config=config,
            canoe=canoe,
            udp_replayer=udp_replayer,
            vehicle=vehicle,
            radar_scene=RadarSceneService(config, vehicle, udp_replayer),
            alarm=AlarmChecker(config, canoe),
            state=StateChecker(config, canoe),
            evidence=EvidenceCollector(config.resolve_path(config.section("paths").get("reports", "../../reports/logs"))),
        )

    def start(self) -> None:
        # 测试开始前的统一动作。
        # 真实模式：打开 CANoe、启动 Measurement、打开 UDP socket。
        # 离线模式：只记录操作，不启动 CANoe。
        self.canoe.open_project()
        self.canoe.start_measurement()
        self.udp_replayer.open()

    def stop(self) -> None:
        # 测试结束后的统一清理动作。
        self.udp_replayer.close()
        self.canoe.close()

    def __enter__(self) -> "HilContext":
        # 支持 with HilContext.create(...) as hil: 写法。
        self.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        # 无论测试通过还是失败，离开 with 时都会清理。
        self.stop()
