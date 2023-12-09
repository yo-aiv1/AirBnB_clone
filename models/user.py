#!/usr/bin/python3
"""Class : User."""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Construct for User."""
        super().__init__(*args, **kwargs)
