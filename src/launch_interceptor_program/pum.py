"""
Preliminary Unlocking Matrix (PUM) computation.
"""

from .model import Connector

def compute_pum(cmv: list[bool], lcm: list[list[Connector]]) -> list[list[bool]]:
    """
    Computes the Preliminary Unlocking Matrix.

    Args:
        cmv: Output of the compute_cmv function
        lcm: The Logical Connector Matrix

    Returns:
        Boolean matrix.
    """
    pum = []
    for (lcm_row, row_lic) in zip(lcm, cmv):
        row = []
        for (col_lic, connector) in zip(cmv, lcm_row):
            connection = True
            if connector == Connector.ORR:
                connection = col_lic or row_lic
            if connector == Connector.ANDD:
                connection = col_lic and row_lic

            row.append(connection)
        pum.append(row)
    return pum
