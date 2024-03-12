#!/usr/bin/python3

"""
test for user model.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Testing Review class
    """

    def test_Review_inheritance(self):
        """
        tests that the Review class Inherits from BaseModel
        """
        reviewbase = Review()
        self.assertIsInstance(reviewbase, BaseModel)

    def test_Review_attributes(self):
        """
        Test that Review class has place_id, user_id and text
        attributes.
        """
        reviewbase = Review()
        self.assertTrue("place_id" in reviewbase.__dir__())
        self.assertTrue("user_id" in reviewbase.__dir__())
        self.assertTrue("text" in reviewbase.__dir__())

    def test_Review_attributes(self):
        """
        test that Review class has place_id, user_id and text
        attributes.
        """
        reviewbase = Review()
        user_id = getattr(reviewbase, "user_id")
        place_id = getattr(reviewbase, "place_id")
        text = getattr(reviewbase, "text")
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(text, str)
        