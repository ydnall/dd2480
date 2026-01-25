"""Tests for LIC 10."""

from launch_interceptor_program.lic.lic_10 import lic_10
from launch_interceptor_program.model import Point, Parameters

def test_lic10_false_few_points():
    points = [(0.0, 0.0)] * 4
    params = Parameters(E_PTS=1, F_PTS=1, AREA1=1.0)
    assert not lic_10(points, params)

def test_lic10_true_large_area():
    # Points forming triangle with area 1.0 > AREA1=0.5
    points = [(0,0), (1,0), (0,2), (2,0)]
    params = Parameters(E_PTS=1, F_PTS=1, AREA1=0.5)
    assert lic_10(points, params)

def test_lic10_false_small_area():
    # Area 0.1 < AREA1=0.5
    points = [(0,0), (1,0), (0,0.2), (2,0)]
    params = Parameters(E_PTS=1, F_PTS=1, AREA1=0.5)
    assert not lic_10(points, params)

