#!/usr/bin/python3
"""
unittest for file_storage by
using a dictionary representation
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models.city import City
from models.amenity import Amenity
from models.place import Place


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    method:
        setUp
        fullClear
        test_all_non_empty
        test_all_empty
    """

    def setUp(self):
        """Set up the test environment.

        Test:
            create a storage.json file
        """
        self.file_path = 'test_storage.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def fullClear(self):
        """Clear Up the test environment.

        Test:
            deletes all json files
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new(self):
        """Test the 'new' method.

        Test:
            new item and test item existance
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.{}'.format(obj.id), self.storage.all())
        obj1 = BaseModel()
        obj2 = City()
        obj3 = Amenity()
        obj4 = Place()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.new(obj4)

        expected_dict = {
            'BaseModel.{}'.format(obj1.id): obj1,
            'City.{}'.format(obj2.id): obj2,
            'Amenity.{}'.format(obj3.id): obj3,
            'Place.{}'.format(obj4.id): obj4
        }

        self.assertDictEqual(self.storage.all(), expected_dict)

    def test_reload(self):
        """Test the 'reload' method.

        Test:
            test reload method
        """
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objs = new_storage.all()
        self.assertIn('BaseModel.{}'.format(obj.id), all_objs)

        obj1 = BaseModel()
        obj2 = City()
        obj3 = Amenity()
        obj4 = Place()

        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.new(obj3)
        self.storage.new(obj4)

        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objs = new_storage.all()
        expected_dict = {
            'BaseModel.{}'.format(obj1.id): obj1,
            'City.{}'.format(obj2.id): obj2,
            'Amenity.{}'.format(obj3.id): obj3,
            'Place.{}'.format(obj4.id): obj4
        }

        self.assertDictEqual(all_objs, expected_dict)


if __name__ == '__main__':
    unittest.main()
