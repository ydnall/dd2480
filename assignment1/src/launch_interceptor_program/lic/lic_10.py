"""
LIC 10: Triangle area with separated points.
"""

from ..model import Point, Parameters
from .geometry import triangle_area


def lic_10(points: list[Point], params: Parameters) -> bool:
    n = len(points)
    if n < 5:
        return False

    e_pts = params.E_PTS
    f_pts = params.F_PTS
    area1 = params.AREA1

    if e_pts < 1 or f_pts < 1 or e_pts + f_pts > n - 3:
        return False

    for i in range(n - e_pts - f_pts - 2):
        j = i + e_pts + 1
        k = j + f_pts + 1

        if triangle_area(points[i], points[j], points[k]) > area1:
            return True

    return False
