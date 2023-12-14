#!/usr/bin/python3
"""City Test unittest for City
test_inheritance from BaseModel
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.

    Test City instantiation, attributes, and additional methods.
    """

    def test_city_instance(self):
        """Test the creation of a City instance."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_default_attributes(self):
        """Check if name and state_id are initially set to None."""
        my_city = City()
        self.assertEqual(my_city.name, "")
        self.assertEqual(my_city.state_id, "")


if __name__ == '__main__':
    unittest.main()
