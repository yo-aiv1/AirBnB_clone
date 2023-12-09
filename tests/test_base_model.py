#!/usr/bin/python3
"""unittest for base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test_BaseModel unite class"""

    def test_instance_type(self):
        """ test type of instances """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_str(self):
        """test str instance """
        my_model = BaseModel()
        frst_str = str(my_model)
        self.assertIn("[BaseModel]", frst_str)
        self.assertIn(str(my_model.id), frst_str)
        self.assertIn(str(my_model.__dict__), frst_str)

    def test_save(self):
        """Test saving mode """
        my_model = BaseModel()
        my_model.save()

    def test_to_dict(self):
        """Test serialization meth"""
        my_model = BaseModel()
        my_model.name = "Y and Z team"
        my_model.my_number = 98
        my_model_json = my_model.to_dict()

        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['id'], my_model.id)
        self.assertEqual(my_model_json['created_at'],
                         my_model.created_at.isoformat()
                         )
        self.assertEqual(my_model_json['updated_at'],
                         my_model.updated_at.isoformat()
                         )
        self.assertEqual(my_model_json['name'], 'Y and Z team')
        self.assertEqual(my_model_json['my_number'], 98)

        """ adding Kwark and get data from to_dic Part """
        my_model = BaseModel(**my_model_json)

        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.id, my_model_json['id'])
        self.assertEqual(my_model.name, my_model_json['name'])
        self.assertEqual(my_model.my_number, my_model_json['my_number'])

    def test_attribute_modification(self):
        """ attr test_attribute_modification test """
        my_model = BaseModel()
        my_model.name = "Test Model"
        self.assertEqual(my_model.name, "Test Model")


if __name__ == '__main__':
    unittest.main()
