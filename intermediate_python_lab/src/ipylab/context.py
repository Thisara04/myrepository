from contextlib import contextmanager
import time
import logging
from typing import Iterator

@contextmanager
def timer(label: str) -> Iterator[None]:
    start = time.perf_counter()   # record start time
    try:
        yield
    finally:
        end = time.perf_counter()
        elapsed_ms = (end - start) * 1000
        logging.info(f"[{label}] took {elapsed_ms:.2f} ms")

@contextmanager
def suppress_and_log(*exc_types: type[BaseException]) -> Iterator[None]:
    try:
        yield
    except exc_types as exc:
        logging.exception(f"Suppressed exception: {exc}")
