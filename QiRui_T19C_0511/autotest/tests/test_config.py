from __future__ import annotations

from pathlib import Path

from autotest.core.config import ProjectConfig, load_yaml


def test_project_config_loads_default_file():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))

    assert config.section("project")["name"] == "Chery_T19C_RLCR_RRCR"
    assert config.canoe_cfg_path().name == "Chery_T19C.cfg"
    assert config.signal("speed").message == "ABS_ESP_1"
    assert config.alarm_signal("rlcr_bsd_warn").signal == "RLCR_1_BSDWarn"


def test_scenario_loads_from_library():
    config = ProjectConfig.load(Path("autotest/project_config/t19c_rlcr_rrcr.yaml"))
    scenario = load_yaml(config.scenario_path("bsd_target_approach_left"))

    assert scenario["case_id"] == "SCN_BSD_LEFT_001"
    assert scenario["objects"][0]["distance_m"] == 12.0

