from launch_interceptor_program.lic.geometry import triangle_area, distance, circumradius


def test_triangle_area_unit_triangle():
    """Unit right triangle should have area 0.5"""
    result = triangle_area((0, 0), (1, 0), (0, 1))
    assert result == 0.5

def test_triangle_area_collinear_points():
    """Collinear points should have area 0"""
    result = triangle_area((0, 0), (1, 1), (2, 2))
    assert result == 0.0

def test_triangle_area_known_triangle():
    """Triangle with base 2, height 3 should have area 3"""
    result = triangle_area((0, 0), (2, 0), (0, 3))
    assert result == 3.0

def test_distance_horizontal():
    """Horizontal distance of 5 units"""
    result = distance((0, 0), (5, 0))
    assert result == 5.0

def test_distance_vertical():
    """Vertical distance of 3 units"""
    result = distance((0, 0), (0, 3))
    assert result == 3.0

def test_distance_diagonal():
    """3-4-5 right triangle diagonal"""
    result = distance((0, 0), (3, 4))
    assert result == 5.0
    
def test_distance_same_point():
    """Same point should have distance 0"""
    result = distance((2, 3), (2, 3))
    assert result == 0.0


def test_circumradius_right_triangle():
    """Right triangle with legs 3,4 has circumradius 2.5 (hypotenuse/2)"""
    result = circumradius((0, 0), (3, 0), (0, 4))
    assert result == 2.5

def test_circumradius_equilateral():
    """Equilateral triangle with side 2: R = a / sqrt(3)"""
    from math import sqrt
    result = circumradius((0, 0), (2, 0), (1, sqrt(3)))
    assert abs(result - 2 / sqrt(3)) < 1e-9

def test_circumradius_collinear():
    """Collinear points: radius = half longest distance"""
    result = circumradius((0, 0), (2, 0), (4, 0))
    assert result == 2.0  # longest dist = 4, radius = 2
    
def test_circumradius_same_point():
    """All same point: radius = 0"""
    result = circumradius((1, 1), (1, 1), (1, 1))
    assert result == 0.0

