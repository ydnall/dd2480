from ..model import Parameters, Points
from .geometry import triangle_area


def lic_3(points: Points, parameters: Parameters) -> bool:
    """
    Ensures at least one set of three consecutive points are vertices of a triangle
    with area greater than AREA1.
    """
    NUMPOINTS = len(points)
    for i in range(NUMPOINTS - 2):
        area = triangle_area(points[i], points[i + 1], points[i + 2])
        if area > parameters.AREA1:
            return True

    return False
