"""
Creates State objects
"""
from typing import Any, Literal

from dstability_toolbox.subsoil import Subsoil


# Tools om state te maken. Bv statepoint toevoegen o.b.v. midden grondlaag

def determine_point_in_polygon():
    """Determines a point in a polygon"""


def create_state_points_from_subsoil(
        subsoil: Subsoil,
        soil_collection: Any,  # TODO: Any vervangen
        state_type: Literal['POP', 'OCR']  # 'Yield Stress' niet want daarbij hoort een coördinaat
):
    """Creates a state point for every layer in the subsoil for which state
    parameters were given."""
