from __future__ import annotations

# 这个文件定义“点云协议插件”。
# 为什么要做插件？
# 不同雷达项目的 UDP 数据格式可能不一样：
# - A 项目可能是 JSON
# - B 项目可能是供应商自定义二进制
# - C 项目可能直接回放 PCAP
# 测试用例不应该关心这些差异，只调用统一的 encode_frame()。

import json
from dataclasses import asdict, dataclass
from typing import Protocol


@dataclass(frozen=True)
class PointCloudObject:
    # 目标 ID，用来区分不同目标。
    object_id: int
    # 目标距离，单位 m。
    distance_m: float
    # 目标相对速度，单位 m/s。负值通常表示靠近。
    velocity_mps: float = 0.0
    # 方位角，单位 deg。左负右正或左正右负要按项目协议确认。
    azimuth_deg: float = 0.0
    # 俯仰角，当前毫米波雷达项目可能用不到，但先保留。
    elevation_deg: float = 0.0
    # 雷达反射强度，单位 dBsm。
    rcs_dbsm: float = 0.0


class PointCloudProtocol(Protocol):
    # 协议名字，用在 YAML 的 udp_point_cloud.protocol 字段。
    name: str

    def encode_frame(self, objects: list[PointCloudObject], timestamp_us: int) -> bytes:
        # 把一帧目标列表编码成 UDP payload。
        # payload 必须是 bytes，因为网络发送的是字节流。
        ...


class JsonPointCloudProtocol:
    """调试用 JSON 协议。

    这个格式不是最终量产雷达协议，只是为了先把框架跑通。
    好处是人可以直接看懂 UDP 内容。
    """

    name = "json_debug"

    def encode_frame(self, objects: list[PointCloudObject], timestamp_us: int) -> bytes:
        # 先把 Python 对象组装成字典，再转 JSON 字符串，最后编码成 ASCII 字节。
        payload = {
            "timestamp_us": timestamp_us,
            "objects": [asdict(obj) for obj in objects],
        }
        return json.dumps(payload, separators=(",", ":")).encode("ascii")


class T19CPointCloudV1Protocol(JsonPointCloudProtocol):
    """T19C 点云协议占位插件。

    等拿到供应商真实 UDP 协议后，只需要重写 encode_frame()。
    测试用例仍然写 hil.radar_scene.play(...)，不用改。
    """

    name = "t19c_pointcloud_v1"


PROTOCOLS = {
    # 协议注册表：字符串名字 -> 协议类。
    # YAML 写 protocol: "t19c_pointcloud_v1" 时，会来这里找对应类。
    JsonPointCloudProtocol.name: JsonPointCloudProtocol,
    T19CPointCloudV1Protocol.name: T19CPointCloudV1Protocol,
}


def build_protocol(name: str) -> PointCloudProtocol:
    # 根据协议名字创建协议对象。
    try:
        return PROTOCOLS[name]()
    except KeyError as exc:
        known = ", ".join(sorted(PROTOCOLS))
        raise ValueError(f"Unknown point-cloud protocol '{name}'. Known: {known}") from exc
