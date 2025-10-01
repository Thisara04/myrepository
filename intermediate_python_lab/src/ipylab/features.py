import numpy as np
from typing import Sequence

def feature_vector(x: np.ndarray) -> list[float]:
    if x.size==0:
        raise ValueError("empty array")
    
    rms = float(np.sqrt(np.mean(x**2)))
    zeroCross = float(np.sum(np.diff(np.sign(x)) != 0))
    PtoP = float(np.max(x) - np.min(x))
    mad = float(np.mean(np.abs(np.diff(x))))

    return[rms,zeroCross,PtoP,mad]