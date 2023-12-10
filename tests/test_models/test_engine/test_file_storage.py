#!/usr/bin/python3
"""
unittest for file_storage by
using a dictionary representation
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


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
        """Set up the test environment."""
        self.file_path = 'test_storage.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def fullClear(self):
        """Clear Up the test environment."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_empty(self):
        """Test the 'all' method with an empty storage."""
        self.assertEqual(self.storage.all(), {})

    def test_all_non_empty(self):
        """Test the 'all' method with a non-empty storage."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertEqual(self.storage.all(),
                         {'BaseModel.{}'.format(obj.id): obj})

    def test_new(self):
        """Test the 'new' method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.{}'.format(obj.id), self.storage.all())

    def test_save(self):
        """Test the 'save' method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.file_path, 'r') as file:
            data = file.read()
            self.assertIn('BaseModel.{}'.format(obj.id), data)

    def test_reload(self):
        """Test the 'reload' method."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        all_objs = new_storage.all()
        self.assertIn('BaseModel.{}'.format(obj.id), all_objs)


if __name__ == '__main__':
    unittest.main()
