"""Tests for LIC 9."""

from launch_interceptor_program.lic.lic_9 import lic_9
from launch_interceptor_program.model import Point, Parameters

def test_lic9_false_few_points():
    points = [(0.0, 0.0)] * 4
    params = Parameters(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert not lic_9(points, params)

def test_lic9_true_angle_too_small():
    # Points: i=(0,0), j=(1,0), k=(1,1) -> angle at j is ~135° < 180°-eps
    points = [(0,0), (1,0), (1,1), (2,0)]
    params = Parameters(C_PTS=1, D_PTS=1, EPSILON=0.1)
    assert lic_9(points, params)
