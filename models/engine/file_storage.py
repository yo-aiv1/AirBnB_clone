#!/usr/bin/python3
"""
The FileStorage class.that serializes instances to a
JSON file and deserializes JSON file to instanes
"""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """Storage class.
    attributes:
        __file_path
        __objects
    methods:
        all
        new
        save
        reload
    """
    __file_path = "file.json"
    __objects = {}
    names = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'State',
             'Review']

    def all(self):
        """Public method to return objects.

        Returns:
            dict: objects
        """
        return self.__objects

    def new(self, obj):
        """Public method to set objets.

        Args:
            obj (object): object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        new_dict = {}

        for key in self.__objects.keys():
            new_dict[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        filepath = FileStorage.__file_path

        new_dict = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity, 'State': State,
                    'Review': Review
                    }

        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    if value['__class__'] in self.names:
                        self.new(new_dict[value['__class__']](**value))

    def count(self, class_name):
        """Count the number of instances of a class."""
        try:
            count = sum(1 for
                        obj in self.__objects.values()
                        if obj.__class__.__name__ == class_name)
            return count
        except Exception as e:
            print(e)

    def get(self, cls, id):
        """Retrieve an instance based on its class name and ID."""
        key = "{}.{}".format(cls, id.strip('"'))
        return self.__objects.get(key)
