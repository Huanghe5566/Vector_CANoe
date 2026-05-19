from __future__ import annotations

# conftest.py 是 pytest 的“公共配置文件”。
# 这里定义命令行参数和公共 fixture。
# fixture 可以理解成 pytest 自动准备好的工具，比如 project_config、hil。

from pathlib import Path

import pytest

from autotest.core.config import ProjectConfig
from autotest.core.test_context import HilContext


DEFAULT_CONFIG = Path(__file__).parent / "project_config" / "t19c_rlcr_rrcr.yaml"


def pytest_addoption(parser):
    # --project-config：指定项目 YAML 配置文件。
    parser.addoption("--project-config", default=str(DEFAULT_CONFIG), help="Project YAML config path.")
    # --real-canoe：不加时使用 dry_run 离线模式；加上后才会真正控制 CANoe。
    parser.addoption("--real-canoe", action="store_true", help="Use real CANoe COM automation.")
    # --canoe-hidden：真实模式下隐藏 CANoe 窗口，CI 或自动化电脑可用。
    parser.addoption("--canoe-hidden", action="store_true", help="Hide CANoe window in real automation.")


def pytest_collection_modifyitems(config, items):
    # 默认跳过标记为 hil 的真实台架用例。
    # 这样运行 python -m pytest 时，只跑离线测试，不会误启动 CANoe 或操作 DUT。
    if config.getoption("--real-canoe"):
        return
    skip_hil = pytest.mark.skip(reason="requires --real-canoe and bench hardware")
    for item in items:
        if "hil" in item.keywords:
            item.add_marker(skip_hil)


@pytest.fixture(scope="session")
def project_config(pytestconfig) -> ProjectConfig:
    # 整个测试会话只加载一次项目配置。
    return ProjectConfig.load(pytestconfig.getoption("--project-config"))


@pytest.fixture
def hil(project_config, pytestconfig):
    # 创建 HIL 上下文。
    # 如果命令行没有 --real-canoe，则 dry_run=True，不启动真实 CANoe。
    dry_run = not pytestconfig.getoption("--real-canoe")
    context = HilContext.create(
        config=project_config,
        dry_run=dry_run,
        canoe_visible=not pytestconfig.getoption("--canoe-hidden"),
    )
    context.start()
    try:
        yield context
    finally:
        context.stop()
