from ..model import Parameters, Points


def lic_5(points: Points, parameters: Parameters) -> bool:
    """
    True if there exists two consecutive points such that:
    X[j] - X[i] < 0, where i = j - 1.
    """
    NUMPOINTS = len(points)
    # at least two points are required
    if NUMPOINTS < 2:
        return False

    for i in range(NUMPOINTS - 1):
        x_i = points[i][0]
        x_j = points[i + 1][0]

        if x_j - x_i < 0:
            return True

    return False
