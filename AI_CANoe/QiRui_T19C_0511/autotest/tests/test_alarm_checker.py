from __future__ import annotations

import threading
import time
from pathlib import Path

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.core.config import ProjectConfig
from autotest.services.alarm_checker import AlarmChecker


def test_alarm_checker_detects_active_signal():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    canoe = CanoeAdapter(config=config, dry_run=True)
    checker = AlarmChecker(config=config, canoe=canoe)
    alarm_ref = config.alarm_signal("rlcr_bsd_warn")
    canoe.set_signal(alarm_ref, 0)

    def activate_later():
        time.sleep(0.03)
        canoe.set_signal(alarm_ref, 1)
        time.sleep(0.04)
        canoe.set_signal(alarm_ref, 1)

    thread = threading.Thread(target=activate_later)
    thread.start()
    result = checker.expect_active(
        "rlcr_bsd_warn",
        timeout_ms=300,
        min_hold_ms=20,
        poll_ms=5,
    )
    thread.join(1.0)

    assert result.passed, result.reason
    assert result.first_active_ms is not None
    assert result.hold_time_ms >= 20


def test_alarm_checker_reports_timeout():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    canoe = CanoeAdapter(config=config, dry_run=True)
    checker = AlarmChecker(config=config, canoe=canoe)
    canoe.set_signal(config.alarm_signal("rlcr_bsd_warn"), 0)

    result = checker.expect_active("rlcr_bsd_warn", timeout_ms=30, min_hold_ms=1, poll_ms=5)

    assert not result.passed
    assert "did not become active" in result.reason

