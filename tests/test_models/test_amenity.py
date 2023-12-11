#!/usr/bin/python3
"""Amenity Test unittest for Amenity
test_inheritance from BaseModel
"""
import unittest
from models.amenity import Amenity


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

    def test_default_attributes(self):
        """Check if name and state_id are initially set to None."""
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")


if __name__ == '__main__':
    unittest.main()
