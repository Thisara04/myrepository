import time
import logging
from functools import wraps
from typing import Callable, TypeVar, ParamSpec, Optional

P = ParamSpec("P")
T = TypeVar("T")

def timed(threshold_ms: Optional[float] = None) -> Callable[[Callable[P, T]], Callable[P, T]]:
    def decorator(fn: Callable[P, T]) -> Callable[P, T]:
        @wraps(fn)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start = time.perf_counter()
            result = fn(*args, **kwargs)
            elapsed_ms = (time.perf_counter() - start) * 1000
            level = logging.WARNING if threshold_ms and elapsed_ms > threshold_ms else logging.INFO
            logging.log(level, f"{fn.__name__} took {elapsed_ms:.2f} ms")
            return result
        return wrapper
    return decorator
