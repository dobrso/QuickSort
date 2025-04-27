import time
import numpy as np
from typing import Callable, Any

def measureTime(func: Callable[..., Any], *args: Any, repeats: int) -> np.ndarray:
    times = []

    for _ in range(repeats):
        timeStart = time.perf_counter()
        func(*args)
        timeEnd = time.perf_counter()

        timeDiff = timeEnd - timeStart
        times.append(timeDiff)

    meanTime = np.mean(times)
    return meanTime

def countIterations(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any) -> Any:
        wrapper.iterationCount += 1

        return func(*args)

    wrapper.iterationCount = 0

    return wrapper
