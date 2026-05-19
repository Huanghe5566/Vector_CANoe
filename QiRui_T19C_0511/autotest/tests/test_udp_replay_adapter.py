from __future__ import annotations

import json
import socket
import threading

from autotest.adapters.udp_replay_adapter import UdpReplayAdapter
from autotest.protocols.pointcloud import PointCloudObject


def test_udp_replayer_sends_frames_to_loopback():
    received: list[bytes] = []
    ready = threading.Event()

    def server(sock: socket.socket):
        ready.set()
        while len(received) < 3:
            data, _addr = sock.recvfrom(4096)
            received.append(data)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(("127.0.0.1", 0))
        sock.settimeout(2.0)
        port = sock.getsockname()[1]
        thread = threading.Thread(target=server, args=(sock,), daemon=True)
        thread.start()
        ready.wait(1.0)

        replayer = UdpReplayAdapter(
            target_ip="127.0.0.1",
            target_port=port,
            cycle_ms=5,
            protocol="json_debug",
        )
        stats = replayer.play_frames(
            [
                [PointCloudObject(object_id=1, distance_m=10.0)],
                [PointCloudObject(object_id=1, distance_m=9.5)],
                [PointCloudObject(object_id=1, distance_m=9.0)],
            ]
        )
        thread.join(1.0)

    assert stats.sent_frames == 3
    assert len(received) == 3
    first_payload = json.loads(received[0].decode("ascii"))
    assert first_payload["objects"][0]["object_id"] == 1

