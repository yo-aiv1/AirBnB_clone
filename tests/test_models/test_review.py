#!/usr/bin/python3
"""Review Test unittest for Review
test_inheritance from BaseModel
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.

    Test Review instantiation, attributes, and additional methods.
    """

    def test_review_instance(self):
        """Test the creation of a Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertTrue(hasattr(review, 'text'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))

    def test_default_attributes(self):
        """Check if name and state_id are initially set to None."""
        my_revi = Review()
        self.assertEqual(my_revi.place_id, "")
        self.assertEqual(my_revi.user_id, "")
        self.assertEqual(my_revi.text, "")


if __name__ == '__main__':
    unittest.main()
