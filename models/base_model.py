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
        my_obj = self.__dict__.copy()
        my_obj['__class__'] = self.__class__.__name__
        my_obj['created_at'] = self.created_at.isoformat()
        my_obj['updated_at'] = self.updated_at.isoformat()
        return my_obj
