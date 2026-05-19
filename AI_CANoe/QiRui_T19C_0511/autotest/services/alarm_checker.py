from __future__ import annotations

# 这个文件负责“报警判定”。
# 注意：报警不能只看某一帧是否等于 1。
# 更稳妥的做法是看：
# - 是否在规定时间内触发
# - 触发后保持了多久
# - 有没有反复跳变，也就是抖动

import time
from typing import Any

from autotest.adapters.canoe_adapter import CanoeAdapter
from autotest.core.config import ProjectConfig
from autotest.core.result import AlarmCheckResult, SignalSample
from autotest.core.timing import monotonic_ms


class AlarmChecker:
    def __init__(self, config: ProjectConfig, canoe: CanoeAdapter):
        self.config = config
        self.canoe = canoe

    def expect_active(
        self,
        logical_name: str,
        timeout_ms: int,
        min_hold_ms: int = 0,
        poll_ms: int = 10,
        max_jitter_count: int | None = None,
    ) -> AlarmCheckResult:
        # 读取 YAML 中报警信号配置。
        # active_values 表示哪些值算“报警激活”。
        alarm_cfg = self.config.alarm(logical_name)
        ref = self.config.alarm_signal(logical_name)
        active_values = set(alarm_cfg.get("active_values", [alarm_cfg.get("expected_active_value", 1)]))

        start_ms = monotonic_ms()
        deadline_ms = start_ms + timeout_ms
        first_active_ms: float | None = None
        last_active_ms: float | None = None
        previous_active = False
        jitter_count = 0
        samples: list[SignalSample] = []

        while monotonic_ms() <= deadline_ms:
            # 按 poll_ms 周期不断读取报警信号。
            elapsed_ms = monotonic_ms() - start_ms
            value = self.canoe.get_signal(ref)
            active = self._is_active(value, active_values)
            samples.append(SignalSample(elapsed_ms=elapsed_ms, value=value, active=active))

            if active:
                # 第一次看到 active=True 时，记录首次触发时间。
                if first_active_ms is None:
                    first_active_ms = elapsed_ms
                last_active_ms = elapsed_ms
            elif previous_active and first_active_ms is not None:
                # 已经触发过，又变成非激活，认为发生一次抖动。
                jitter_count += 1

            if first_active_ms is not None and last_active_ms is not None:
                # 计算保持时间。如果保持时间够长，并且抖动次数没超限，就判定通过。
                hold_time_ms = last_active_ms - first_active_ms
                jitter_ok = max_jitter_count is None or jitter_count <= max_jitter_count
                if hold_time_ms >= min_hold_ms and jitter_ok:
                    return AlarmCheckResult(
                        passed=True,
                        reason="Alarm became active within the expected window.",
                        signal_name=logical_name,
                        first_active_ms=first_active_ms,
                        hold_time_ms=hold_time_ms,
                        jitter_count=jitter_count,
                        samples=samples,
                    )

            previous_active = active
            time.sleep(poll_ms / 1000.0)

        hold_time_ms = 0.0
        if first_active_ms is not None and last_active_ms is not None:
            hold_time_ms = last_active_ms - first_active_ms
        if first_active_ms is None:
            # 从头到尾都没触发。
            reason = f"Alarm '{logical_name}' did not become active within {timeout_ms} ms."
        else:
            # 触发了，但保持时间不够。
            reason = f"Alarm '{logical_name}' active hold time {hold_time_ms:.1f} ms is below {min_hold_ms} ms."
        return AlarmCheckResult(
            passed=False,
            reason=reason,
            signal_name=logical_name,
            first_active_ms=first_active_ms,
            hold_time_ms=hold_time_ms,
            jitter_count=jitter_count,
            samples=samples,
        )

    @staticmethod
    def _is_active(value: Any, active_values: set[Any]) -> bool:
        # CANoe 读出来的值可能是 int，也可能是字符串。
        # 这里同时比较原始值和字符串值，减少类型差异导致的误判。
        return value in active_values or str(value) in {str(item) for item in active_values}
