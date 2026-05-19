from __future__ import annotations

from pathlib import Path

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.core.config import ProjectConfig
from autotest.services.state_checker import StateChecker


def test_state_checker_reads_configured_state_name():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    canoe = CanoeAdapter(config=config, dry_run=True)
    checker = StateChecker(config=config, canoe=canoe)
    canoe.set_signal(checker.state_signal(), 2)

    assert checker.read_state_name() == "active"

