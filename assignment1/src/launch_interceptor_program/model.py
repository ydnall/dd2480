"""
Shared input/output types for the Launch Interceptor Program.

These types model the DECIDE() inputs and outputs defined in the spec.
"""

from dataclasses import dataclass
from enum import IntEnum
from typing import List, Sequence, Tuple


Point = Tuple[float, float]


class Connector(IntEnum):
    NOTUSED = 777
    ORR = 778
    ANDD = 779


@dataclass(frozen=True)
class Parameters:
    """Parameter bundle used by LIC evaluations."""
    LENGTH1: float
    RADIUS1: float
    EPSILON: float
    AREA1: float
    Q_PTS: int
    QUADS: int
    DIST: float
    N_PTS: int
    K_PTS: int
    A_PTS: int
    B_PTS: int
    C_PTS: int
    D_PTS: int
    E_PTS: int
    F_PTS: int
    G_PTS: int
    LENGTH2: float
    RADIUS2: float
    AREA2: float


@dataclass(frozen=True)
class DecisionInput:
    """Grouped inputs for a DECIDE() evaluation."""
    points: Sequence[Point]
    parameters: Parameters
    lcm: Sequence[Sequence[Connector]]
    puv: Sequence[bool]


@dataclass(frozen=True)
class DecisionResult:
    """DECIDE() output and intermediate vectors."""
    launch: bool
    cmv: List[bool]
    pum: List[List[bool]]
    fuv: List[bool]
