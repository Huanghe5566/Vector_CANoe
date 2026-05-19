from __future__ import annotations

# 这个文件定义“结果数据结构”。
# dataclass 可以理解为“自动帮你生成 __init__ 的小表格类”。
# 它们只负责保存数据，不负责复杂逻辑。

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SignalSample:
    # elapsed_ms：从开始检查到当前采样点经过了多少毫秒。
    elapsed_ms: float
    # value：这一刻读到的原始信号值。
    value: object
    # active：这一刻是否被认为是报警激活。
    active: bool


@dataclass
class AlarmCheckResult:
    # passed：报警检查是否通过。
    passed: bool
    # reason：通过或失败原因，失败时 pytest 会显示这段文字。
    reason: str
    # signal_name：检查的是哪个逻辑报警名。
    signal_name: str
    # first_active_ms：第一次触发的时间；没触发就是 None。
    first_active_ms: float | None = None
    # hold_time_ms：报警连续保持的时间。
    hold_time_ms: float = 0.0
    # jitter_count：报警触发后又掉下去的次数。
    jitter_count: int = 0
    # samples：整个等待过程中的采样记录，便于失败后分析。
    samples: list[SignalSample] = field(default_factory=list)
