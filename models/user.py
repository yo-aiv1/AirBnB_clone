#!/usr/bin/python3
"""Class : User.
inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class inherits from BaseModel.
    Public class attributes:
        email
        password
        first_name
        last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
