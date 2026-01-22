"""
Top-level DECIDE() entrypoint for the Launch Interceptor Program.
"""

from .model import DecisionInput, DecisionResult


def decide(inputs: DecisionInput) -> DecisionResult:
    """
    Determines if an interceptor will be launched based upon
    input rader tracking information.

    Args:
        inputs: DecisionInput(points, parameters, lcm, puv)

    Returns:
        DecisionResult(launch, cmv, pum, fuv)
    """
    raise NotImplementedError("DECIDE logic not implemented yet")
