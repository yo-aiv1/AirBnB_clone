#!/usr/bin/python3
"""
Class : Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity"""
        super().__init__(*args, **kwargs)
        self.name = ""
