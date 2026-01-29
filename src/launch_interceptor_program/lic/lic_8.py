from ..model import Parameters, Points
from .geometry import min_enclosing_circle_radius


def lic_8(points: Points, parameters: Parameters):
    NUMPOINTS = len(points)
    A_PTS = parameters.A_PTS
    B_PTS = parameters.B_PTS
    RADIUS1 = parameters.RADIUS1

    if NUMPOINTS < 5:
        return False

    if not (A_PTS + B_PTS) <= (NUMPOINTS - 3):
        raise ValueError(
            "(A_PTS + B_PTS) must be less than or equal to (NUMPOINTS - 3)"
        )

    for start_index in range(0, NUMPOINTS - A_PTS - B_PTS - 2):
        first_point = points[start_index]
        second_point = points[start_index + A_PTS + 1]
        third_point = points[start_index + A_PTS + B_PTS + 2]
        radius = min_enclosing_circle_radius(first_point, second_point, third_point)

        if radius > RADIUS1:
            return True

    return False
