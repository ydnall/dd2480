"""
Geometric helper functions for LIC evaluations.

Provides common calculations including areas, distances, etc.
"""

from math import acos, hypot, pow, sqrt

from ..model import Point


def triangle_area(p1: Point, p2: Point, p3: Point) -> float:
    """
    Calculate the area of a triangle formed by three points.

    Uses the shoelace formula: 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|

    Returns 0.0 for collinear points.
    """
    # unpack coordinates from points
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # apply shoelace formula
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    return area


# Needed for lic 4
def quadrant(p: Point) -> int:
    """
    Return the quadrant index of point p based on its (x, y) coordinates.
    """
    x, y = p
    if x >= 0 and y >= 0:
        return 1
    if x < 0 and y >= 0:
        return 2
    if x <= 0 and y < 0:
        return 3
    return 4


def distance(p1: Point, p2: Point) -> float:
    """Euclidean distance between two points."""

    # unpack coordinates from points
    x1, y1 = p1
    x2, y2 = p2

    # apply euclidean distance formula
    dist = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

    return dist


def point_line_distance(p1: Point, start_point: Point, end_point: Point):
    """
    Calculate the distance from a point to a line between two points.

    Uses the area of a parallelogram consisting of vectors from the points divided by the length of the line
    """

    x1, y1 = p1
    x2, y2 = start_point
    x3, y3 = end_point

    line_distance = distance(start_point, end_point)
    parallellogram_area = abs((x3 - x2) * (y2 - y1) - (x2 - x1) * (y3 - y2))
    point_distance = parallellogram_area / line_distance

    return point_distance


def angle(p1: Point, vertex: Point, p3: Point) -> float:
    """
    Calculate the angle (in radians) formed by three points.

    The angle is measured at `vertex`, between the line segments
    (vertex -> p1) and (vertex -> p3).

    If p1 or p3 coincides with the vertex, the angle is undefined and
    0.0 is returned.
    """
    vx1 = p1[0] - vertex[0]
    vy1 = p1[1] - vertex[1]
    vx2 = p3[0] - vertex[0]
    vy2 = p3[1] - vertex[1]

    dot = vx1 * vx2 + vy1 * vy2
    norm1 = hypot(vx1, vy1)
    norm2 = hypot(vx2, vy2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    cos_theta = max(-1.0, min(1.0, dot / (norm1 * norm2)))
    return acos(cos_theta)


def circumradius(p1: Point, p2: Point, p3: Point) -> float:
    """
    Radius of the smallest circle that can contain three points.

    For non-collinear points: circumradius of the triangle.
    For collinear points: infinite (cannot form a circumscribed circle).
    For obtuse and right triangles: half the longest distance.
    """
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p1, p3)
    a, b, c = sorted([a, b, c])

    area = triangle_area(p1, p2, p3)
    eps = 1e-12

    if area <= eps:
        return c / 2.0

    if pow(c, 2) >= pow(a, 2) + pow(b, 2):
        return c / 2.0

    return (a * b * c) / (4.0 * area)
