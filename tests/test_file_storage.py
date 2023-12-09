#!/usr/bin/python3
""" unittest for file_storage """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """unittest for file_storage class """

    def test_new_and_save(self):
        """test new items and save """
        self.storage = FileStorage()
        my_model = BaseModel()
        my_model.name = "Test Model"
        my_model.my_number = 98

        self.storage.new(my_model)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn('Test Model', data)
            self.assertIn('98', data)


if __name__ == '__main__':
    unittest.main()
