"""
Geometric helper functions for LIC evaluations.

Provides common calculations including areas, distances, etc.
"""

from math import sqrt, pow
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

def distance(p1: Point, p2: Point) -> float:
    """Euclidean distance between two points."""

    # unpack coordinates from points
    x1, y1 = p1
    x2, y2 = p2

    # apply euclidean distance formula
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    
    return distance

def circumradius(p1: Point, p2: Point, p3: Point) -> float:
    """
    Radius of the smallest circle that can contain three points.

    For non-collinear points: circumradius of the triangle.
    For collinear points: half the longest distance.
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