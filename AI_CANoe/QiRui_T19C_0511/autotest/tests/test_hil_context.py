from __future__ import annotations

from pathlib import Path

from autotest.core.config import ProjectConfig
from autotest.core.test_context import HilContext


def test_hil_context_starts_in_dry_run():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    context = HilContext.create(config=config, dry_run=True)

    with context as hil:
        hil.vehicle.set_speed(12.5)
        assert hil.canoe.operation_log[0][0] == "open_project"
        assert hil.canoe.get_signal(config.signal("speed")) == 12.5

