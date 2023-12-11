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

    def test_default_attributes(self):
        """Check if name and state_id are initially set to None."""
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenities, [])


if __name__ == '__main__':
    unittest.main()
