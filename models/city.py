#!/usr/bin/python3
"""Class : City.
Public class attributes
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class inherits from BaseModel.
    Public class attributes:
        state_id
        name
    """

    state_id = ""
    name = ""
