from __future__ import annotations

from pathlib import Path

from autotest.core.config import ProjectConfig
from autotest.core.test_context import HilContext


def test_radar_scene_applies_vehicle_inputs():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    context = HilContext.create(config=config, dry_run=True)
    scenario = context.radar_scene.load("empty_scene")

    context.radar_scene.apply_vehicle(scenario)

    assert context.canoe.get_signal(config.signal("speed")) == 0
    assert context.canoe.get_signal(config.signal("gear")) == 1
    assert context.canoe.get_signal(config.signal("bsd_lca_rcta_switch")) == 0

