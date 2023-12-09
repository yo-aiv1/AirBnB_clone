#!/usr/bin/python3
"""Class : State."""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class inherits from BaseModel."""

    def __init__(self, *args, **kwargs):
        """Construct for State."""
        super().__init__(*args, **kwargs)
        self.name = ""
