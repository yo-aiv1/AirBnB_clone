#!/usr/bin/python3
"""
Class : Review
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Review Class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Review"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
