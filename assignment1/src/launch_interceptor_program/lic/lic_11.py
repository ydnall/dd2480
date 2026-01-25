"""
LIC 11: X decreases over G_PTS points.
"""

from ..model import Parameters, Point


def lic_11(points: list[Point], params: Parameters) -> bool:
    n = len(points)
    if n < 3:
        return False

    g_pts = params.G_PTS
    if g_pts < 1 or g_pts > n - 2:
        return False

    for i in range(n - g_pts - 1):
        j = i + g_pts + 1
        if points[j][0] < points[i][0]:  # Xj - Xi < 0
            return True

    return False
