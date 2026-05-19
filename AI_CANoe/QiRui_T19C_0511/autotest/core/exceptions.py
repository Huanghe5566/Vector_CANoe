# 这个文件统一定义框架自己的异常类型。
# 异常可以理解为“程序发现问题后抛出的错误”。
# 单独定义这些类的好处是：以后看到 ConfigError、CanoeError，就知道问题大概在哪一层。

class AutotestError(Exception):
    """Base exception for the automation framework."""


class ConfigError(AutotestError):
    # 配置文件错误，例如 YAML 路径不存在、字段缺失、格式写错。
    """Raised when project or scenario configuration is invalid."""


class CanoeError(AutotestError):
    # CANoe 控制错误，例如 CANoe COM 启动失败、信号名找不到。
    """Raised when CANoe automation fails."""


class UdpReplayError(AutotestError):
    # UDP 回灌错误，例如 IP/端口配置缺失、场景持续时间非法。
    """Raised when UDP point-cloud replay fails."""


class CheckError(AutotestError):
    # 判定逻辑错误，例如等待一个配置里不存在的状态。
    """Raised when a checker cannot evaluate a result."""
