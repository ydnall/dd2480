"""
Tests for the pum computation.
"""

from launch_interceptor_program.pum import compute_pum
from launch_interceptor_program.model import Connector

def test_pum_4x4_mixed_values():
    """
    Test with 4x4 matrix without NOTUSED.
    """
    cmv = [True, False, True, False]

    lcm = [
        [Connector.ANDD, Connector.ORR,  Connector.ANDD, Connector.ORR],
        [Connector.ORR,  Connector.ANDD, Connector.ORR,  Connector.ANDD],
        [Connector.ANDD, Connector.ANDD, Connector.ORR,  Connector.ORR],
        [Connector.ORR,  Connector.ORR,  Connector.ANDD, Connector.ANDD],
    ]

    pum = compute_pum(cmv, lcm)

    expected = [
        [True,  True,  True,  True],
        [True,  False, True,  False],
        [True,  False, True,  True],
        [True,  False, False,  False],
    ]

    assert pum == expected


def test_pum_5x5_with_notused():
    """
    Test with 5x5 matrix.
    """

    cmv = [True, False, False, True, False]

    lcm = [
        [Connector.NOTUSED]*5,
        [Connector.ANDD]*5,
        [Connector.ORR]*5,
        [Connector.NOTUSED, Connector.ANDD, Connector.ORR, Connector.NOTUSED, Connector.ANDD],
        [Connector.ORR, Connector.NOTUSED, Connector.ANDD, Connector.ORR, Connector.NOTUSED],
    ]

    pum = compute_pum(cmv, lcm)

    expected = [
        [True, True, True, True, True],
        [False, False, False, False, False],
        [True, False, False, True, False],
        [True, False, True, True, False],
        [True, True, False, True, True],
    ]

    assert pum == expected



def test_pum_all_false_cmv():
    """
    Test with fully False cmv.
    """

    cmv = [False, False, False]

    lcm = [
        [Connector.ANDD, Connector.ORR,  Connector.ANDD],
        [Connector.ORR,  Connector.ANDD, Connector.ORR],
        [Connector.ANDD, Connector.ANDD, Connector.ORR],
    ]

    pum = compute_pum(cmv, lcm)

    expected = [
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]

    assert pum == expected


def test_pum_all_true_cmv():
    """
    Test with fully True cmv.
    """


    cmv = [True, True, True, True]

    lcm = [
        [Connector.ANDD]*4,
        [Connector.ORR]*4,
        [Connector.ANDD]*4,
        [Connector.ORR]*4,
    ]

    pum = compute_pum(cmv, lcm)

    assert pum == [[True]*4 for _ in range(4)]


def test_pum_single_element():

    cmv = [False]
    lcm = [[Connector.ANDD]]

    pum = compute_pum(cmv, lcm)

    assert pum == [[False]]


def test_pum_empty():
    pum = compute_pum([], [])
    assert pum == []
