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