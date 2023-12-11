#!/usr/bin/python3
"""Amenity Test unittest for Amenity
test_inheritance from BaseModel
"""
import unittest
from models.city import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.

    Test Amenity instantiation, attributes, and additional methods.
    """

    def test_amenity_instance(self):
        """Test the creation of an Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(hasattr(amenity, 'name'))


if __name__ == '__main__':
    unittest.main()
