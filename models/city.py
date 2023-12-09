#!/usr/bin/python3
"""Class : City."""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Construct for City."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
