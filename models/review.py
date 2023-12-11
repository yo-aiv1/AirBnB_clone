#!/usr/bin/python3
"""Class : Review.
Public class attributes inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class inherits from BaseModel.
    Public class attributes:
        place_id
        user_id
        text
    """

    place_id = ""
    user_id = ""
    text = ""
