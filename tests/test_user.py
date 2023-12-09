#!/usr/bin/python3
"""User Test"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ unittest testing for TestUser """

    def test_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """ testing test_inheritance """
        user = User()
        self.assertIsInstance(user, BaseModel)


if __name__ == '__main__':
    unittest.main()
