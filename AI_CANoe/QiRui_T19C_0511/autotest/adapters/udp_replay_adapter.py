from __future__ import annotations

# 这个文件负责“UDP 点云回灌”。
# 可以把它想象成一个小喇叭：Python 按固定周期，把目标点云数据通过 UDP 发给雷达。
# 当前版本先支持 Python 直接发 UDP；如果以后周期抖动太大，可以把这个类背后的发送实现换成 C++/Rust。

import socket
import time
from dataclasses import dataclass, field
from typing import Any

from autotest.core.exceptions import UdpReplayError
from autotest.core.timing import PeriodicClock
from autotest.protocols.pointcloud import PointCloudObject, PointCloudProtocol, build_protocol


@dataclass
class UdpReplayStats:
    # 已发送的帧数。帧可以理解为一次 UDP 数据包。
    sent_frames: int = 0
    # 已发送的总字节数。
    sent_bytes: int = 0
    # 期望发送周期，比如 50 ms。
    cycle_ms: float = 0.0
    # 最大周期抖动。例：期望 50 ms，实际 53 ms，抖动就是 3 ms。
    max_period_jitter_ms: float = 0.0
    # 每两帧之间的实际时间间隔列表，用于后续分析时序稳定性。
    periods_ms: list[float] = field(default_factory=list)


class UdpReplayAdapter:
    """独立 UDP 点云回灌服务。

    这个类只关心“向哪个 IP/端口发、多久发一次、发什么数据”。
    它不直接关心 CANoe，也不直接关心测试断言。
    """

    def __init__(
        self,
        target_ip: str,
        target_port: int,
        cycle_ms: float,
        protocol: str | PointCloudProtocol = "json_debug",
        bind_ip: str | None = None,
    ):
        # UDP 目标地址，也就是雷达或本地测试 UDP 服务器的 IP/端口。
        self.target = (target_ip, int(target_port))
        # 发送周期，单位 ms。
        self.cycle_ms = float(cycle_ms)
        # protocol 是点云编码插件。
        # 现在的 t19c_pointcloud_v1 先用 JSON 调试格式，后续拿到真实协议后只改插件。
        self.protocol = build_protocol(protocol) if isinstance(protocol, str) else protocol
        # bind_ip 是本机网卡 IP。一般真实台架需要指定，离线测试可以不指定。
        self.bind_ip = bind_ip
        self.stats = UdpReplayStats(cycle_ms=self.cycle_ms)
        # _sock 是 Python UDP socket。None 表示还没打开。
        self._sock: socket.socket | None = None

    @classmethod
    def from_config(cls, udp_config: dict[str, Any]) -> "UdpReplayAdapter":
        # 从 YAML 的 udp_point_cloud 章节创建 UDP 回灌器。
        # 这样测试代码不用写死 IP、端口和周期。
        try:
            return cls(
                target_ip=udp_config["target_ip"],
                target_port=int(udp_config["target_port"]),
                bind_ip=udp_config.get("local_ip"),
                cycle_ms=float(udp_config.get("cycle_ms", 50)),
                protocol=udp_config.get("protocol", "json_debug"),
            )
        except KeyError as exc:
            raise UdpReplayError(f"Missing UDP config key: {exc.args[0]}") from exc

    def open(self) -> None:
        # 打开 UDP socket。
        # UDP 不需要像 TCP 那样 connect，它更像“写好地址直接投递包裹”。
        if self._sock is not None:
            return
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if self.bind_ip:
            # 指定从哪块网卡发出。真实台架有多网卡时很重要。
            self._sock.bind((self.bind_ip, 0))

    def close(self) -> None:
        # 关闭 socket，释放系统资源。
        if self._sock is not None:
            self._sock.close()
            self._sock = None

    def send_frame(self, objects: list[PointCloudObject], timestamp_us: int | None = None) -> int:
        # 发送一帧点云。
        # objects 是这一帧里所有目标，比如一个车、一个行人、一个空目标列表。
        self.open()
        assert self._sock is not None
        # 如果调用方没给时间戳，就用当前电脑时间，单位微秒。
        timestamp = timestamp_us if timestamp_us is not None else int(time.time() * 1_000_000)
        # 把 Python 对象编码成 bytes，才能通过 UDP 发送。
        payload = self.protocol.encode_frame(objects, timestamp)
        sent = self._sock.sendto(payload, self.target)
        # 更新统计信息，便于测试报告记录。
        self.stats.sent_frames += 1
        self.stats.sent_bytes += sent
        return sent

    def play_scenario(self, scenario: dict[str, Any]) -> UdpReplayStats:
        # 播放一个 YAML 场景。
        # 场景中 objects 写目标列表，duration_ms 写持续时间。
        objects = [self._object_from_mapping(item) for item in scenario.get("objects", [])]
        duration_ms = int(scenario.get("duration_ms", self.cycle_ms))
        if duration_ms <= 0:
            raise UdpReplayError("scenario.duration_ms must be greater than 0.")
        frames = max(1, int(round(duration_ms / self.cycle_ms)))
        # 简化处理：当前版本每一帧都发送同一批目标。
        # 后续可扩展成每帧目标位置变化的轨迹回放。
        return self.play_frames([objects] * frames)

    def play_frames(self, frames: list[list[PointCloudObject]]) -> UdpReplayStats:
        # 播放多帧点云，同时统计每帧间隔。
        self.stats = UdpReplayStats(cycle_ms=self.cycle_ms)
        clock = PeriodicClock(self.cycle_ms)
        last_send_s: float | None = None
        for objects in frames:
            now_s = time.perf_counter()
            if last_send_s is not None:
                # 计算上一帧到这一帧的实际时间间隔。
                period_ms = (now_s - last_send_s) * 1000.0
                self.stats.periods_ms.append(period_ms)
                self.stats.max_period_jitter_ms = max(
                    self.stats.max_period_jitter_ms,
                    abs(period_ms - self.cycle_ms),
                )
            self.send_frame(objects)
            last_send_s = now_s
            # 等到下一个周期点再继续发。
            clock.wait_next()
        return self.stats

    @staticmethod
    def _object_from_mapping(data: dict[str, Any]) -> PointCloudObject:
        # 把 YAML 里的目标配置转换成 Python 点云目标对象。
        # data.get("xxx", 默认值) 的意思是：如果 YAML 没写这个字段，就用默认值。
        return PointCloudObject(
            object_id=int(data.get("id", data.get("object_id", 0))),
            distance_m=float(data.get("distance_m", 0.0)),
            velocity_mps=float(data.get("velocity_mps", 0.0)),
            azimuth_deg=float(data.get("azimuth_deg", 0.0)),
            elevation_deg=float(data.get("elevation_deg", 0.0)),
            rcs_dbsm=float(data.get("rcs_dbsm", 0.0)),
        )

    def __enter__(self) -> "UdpReplayAdapter":
        # 支持 with UdpReplayAdapter(...) as replayer: 这种写法。
        # 进入 with 时自动打开 socket。
        self.open()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        # 离开 with 时自动关闭 socket。
        self.close()
