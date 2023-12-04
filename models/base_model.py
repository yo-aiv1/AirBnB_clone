#!/usr/bin/python3
"""BaseModel class for the Airbnb clone."""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class."""

    def __init__(self):
        """Initialize a new instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Will return information about the class."""
        classname = "{}".format(self.__class__.__name__)
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Update updated_at time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return new dictionary.

        containing all keys/values of __dict__ of the instance.
        """
        result = {}
        f = "%Y-%m-%dT%H:%M:%S.%f"
        for key in self.__dict__.keys():
            if key == "updated_at" or key == "created_at":
                value = self.__dict__[key]
                new_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                result[key] = new_value
            else:
                result[key] = self.__dict__[key]

        return result
