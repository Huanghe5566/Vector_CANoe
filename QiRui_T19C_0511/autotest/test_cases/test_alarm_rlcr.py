from __future__ import annotations

# 这是一个真实 HIL 用例示例。
# pytest 会把 conftest.py 中的 hil fixture 传进来。
# hil 就是测试工具箱，里面包含 CANoe、UDP 回灌、报警检查等能力。

import pytest

from autotest.core.config import load_yaml

pytestmark = pytest.mark.hil
# 上面这行表示：本文件里的用例都属于真实台架 HIL 用例。
# 不加 --real-canoe 时会自动跳过，防止误操作真实设备。


def test_rlcr_bsd_warning_with_left_target(hil):
    # 1. 读取场景文件。
    # bsd_target_approach_left 对应 autotest/scenario_library/bsd_target_approach_left.yaml。
    scenario = load_yaml(hil.config.scenario_path("bsd_target_approach_left"))

    # 2. 播放场景。
    # 这里会自动设置车速/档位/开关，并通过 UDP 发送点云目标。
    hil.radar_scene.play(scenario)

    # 3. 从场景里取期望结果，例如希望 rlcr_bsd_warn 在 1500 ms 内触发。
    expected = scenario["expected"]

    # 4. 检查报警是否按要求触发，并记录触发时间、保持时间、抖动次数。
    result = hil.alarm.expect_active(
        expected["alarm"],
        timeout_ms=expected["trigger_within_ms"],
        min_hold_ms=expected["min_hold_ms"],
    )

    # 5. 保存证据 JSON，便于失败后复盘。
    hil.evidence.write_json("rlcr_bsd_warning_with_left_target", {"result": result})

    # 6. pytest 断言。result.passed 为 False 时，用 result.reason 输出失败原因。
    assert result.passed, result.reason
