#!/usr/bin/python3
"""State Test"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """State test class"""

    def test_attributes(self):
        """ test attr"""
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        """ test test_inheritance """
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
