#!/usr/bin/python3
"""State Test unittest for State
test_inheritance from BaseModel
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """State test class unittest
    Test:
        test_attributes
        test_inheritance
    """

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
