#!/usr/bin/python3
"""User Test unittest for user

    Test:
        test_inheritance
        test_attributes
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ unittest testing for TestUser

    Test:
        test_attributes
        test_inheritance
        test_id_is_public_str
    """

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

    def test_id_is_public_str(self):
        """ Testing Id is str"""
        self.assertEqual(str, type(User().id))


if __name__ == '__main__':
    unittest.main()
