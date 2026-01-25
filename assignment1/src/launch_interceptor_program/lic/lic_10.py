"""
LIC 10: Triangle area with separated points.
"""

from ..model import Parameters, Point
from .geometry import triangle_area


def lic_10(points: list[Point], params: Parameters) -> bool:
    NUMPOINTS = len(points)
    if NUMPOINTS < 5:
        return False

    E_PTS = params.E_PTS
    F_PTS = params.F_PTS
    AREA1 = params.AREA1

    if E_PTS < 1 or F_PTS < 1 or E_PTS + F_PTS > NUMPOINTS - 3:
        return False

    for i in range(NUMPOINTS - E_PTS - F_PTS - 2):
        j = i + E_PTS + 1
        k = j + F_PTS + 1

        if triangle_area(points[i], points[j], points[k]) > AREA1:
            return True

    return False
