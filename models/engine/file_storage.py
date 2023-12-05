#!/usr/bin/python3
"""Storage class."""
import json
import os.path


class FileStorage:
    """The FileStorage class."""

    __file_path = "file.json"
    __objects = {}

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
        key = "{}.{}".format(__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        new_dict = {}

        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key]

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_data = f.read()
            FileStorage.__objects = json.loads(json_data)
