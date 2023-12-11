#!/usr/bin/python3
"""Place Test unittest for Place
test_inheritance from BaseModel
"""
import unittest
from models.place import Place
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.

    Test Place instantiation, attributes, and additional methods.
    """

    def test_place_instance(self):
        """Test the creation of a Place instance."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))


if __name__ == '__main__':
    unittest.main()
