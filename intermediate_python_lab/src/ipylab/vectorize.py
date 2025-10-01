from typing import Sequence
import numpy as np
import math

def python_rms(seq: Sequence[float]) -> float:
    n = len(seq)
    if n==0:
        raise ValueError("empty array")
    total = sum(x*x for x in seq)
    return math.sqrt(total / n)
    

def numpy_rms(arr: np.ndarray) -> float:
    if arr.size==0:
        raise ValueError("empty array")
    return float(np.sqrt(np.mean(arr**2)))
    
