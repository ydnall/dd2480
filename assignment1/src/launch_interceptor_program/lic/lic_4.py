from ..model import Parameters, Points
from .geometry import get_quadrant 

def lic_4(points: Points, parameters: Parameters) -> bool:
    """
    Checks if there exists a set of Q_PTS consecutive points 
    that lie in more than QUADS quadrants.
    """
    if len(points) < parameters.Q_PTS:
        return False
    for i in range(len(points) - parameters.Q_PTS + 1):
        
        quadrants_in_window = set()
        
        for j in range(parameters.Q_PTS):
            current_point = points[i + j]
            q = get_quadrant(current_point)
            quadrants_in_window.add(q)
            
        if len(quadrants_in_window) > parameters.QUADS:
            return True
        
    return False
    

