#!/usr/bin/python3
"""
BaseModel Modul is the parent class for all entities within
the AirBnB clone, providing foundational attributes and methods
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel Class.
    Public instance:
        id
        created_at
        updated_at
    methods:
        __str__
        save
        to_dict
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new instance.

        Returns:
            BaseModel(id, created_at, updated_at) obj
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Will return information about the class.

        Return:
        print: [<class name>] (<self.id>) <self.__dict__>
        """
        classname = "{}".format(self.__class__.__name__)
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Update updated_at time.

        Return:
            updated_at time and save file.json data

        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return new dictionary.

        containing all keys/values of __dict__ of the instance.
        """
        result = {}
        result['__class__'] = type(self).__name__
        for key in self.__dict__.keys():
            if key == "updated_at" or key == "created_at":
                value = self.__dict__[key]
                new_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                result[key] = new_value
            else:
                result[key] = self.__dict__[key]

        return result
