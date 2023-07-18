from typing import List
import numpy as np

def nurb_naive(u: float, k: int, p: int, knots: List[float]) -> float: ...
def nurb_iterative(u: float, k: int, p: int, knots: List[float]) -> float: ...

class ControlPoint:
    x: float
    y: float
    z: float
    w: float
    
    def __init__(self, x: float, y: float, z: float, w: float) -> None: ...

class Nurb:
    degree: int
    knots: List[float]
    control_points: List[ControlPoint]
    
    def __init__(self, degree: int, knots: float, control_points: List[ControlPoint]) -> None: ...
    def rasterize(self, resolution: int) -> List[ControlPoint]: ...
    def rasterize_to_numpy(self, resolution: int) -> np.ndarray: ...
