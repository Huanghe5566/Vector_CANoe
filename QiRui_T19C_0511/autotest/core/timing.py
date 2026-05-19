from __future__ import annotations

# 这个文件放和时间有关的小工具。
# 自动化测试里时间很重要：
# - UDP 要按 50 ms/100 ms 周期发
# - 报警要在规定时间内触发
# - 状态机要在规定时间内跳转

import time


def monotonic_ms() -> float:
    # perf_counter() 是单调递增时钟，不会因为系统时间被手动修改而倒退。
    # 乘以 1000 是把秒转换成毫秒。
    return time.perf_counter() * 1000.0


def sleep_until(target_s: float) -> None:
    # 睡到指定时间点。
    # 如果目标时间已经过去，就不睡，直接返回。
    delay = target_s - time.perf_counter()
    if delay > 0:
        time.sleep(delay)


class PeriodicClock:
    """固定周期循环助手。

    例如周期 50 ms：
    每发一帧 UDP 后调用 wait_next()，它会尽量等到下一个 50 ms 周期点。
    """

    def __init__(self, cycle_ms: float):
        # 把毫秒转换成秒，因为 time.perf_counter() 的单位是秒。
        self.cycle_s = cycle_ms / 1000.0
        # next_s 表示下一次应该执行的时间点。
        self.next_s = time.perf_counter()

    def wait_next(self) -> float:
        # 计算下一个周期点，然后睡到那个时间。
        self.next_s += self.cycle_s
        sleep_until(self.next_s)
        return time.perf_counter()
