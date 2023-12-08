#!/usr/bin/python3
"""Storage class."""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """The FileStorage class."""

    __file_path = "file.json"
    __objects = {}
    names = ['BaseModel', 'User']

    def all(self):
        """Public method to return objects.

        Returns:
            dict: objects
        """
        return FileStorage.__objects

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

        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        filepath = FileStorage.__file_path
        fileobject = FileStorage.__objects
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    if value['__class__'] in self.names:
                        fileobject[key] = eval(value['__class__'])(**value)
