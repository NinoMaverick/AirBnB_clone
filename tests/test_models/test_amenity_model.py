#!/usr/bin/python3

"""
    test for the amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Testing Amenity class
    """

    def test_Amenityinherit(self):
        """
        tests that the Amenity class Inherits from BaseModel
        """ 
        amenitybase = Amenity()
        self.assertIsInstance(amenitybase, BaseModel)

    def test_Amenityattr(self):
        """
        Test that Amenity class attribute.
        """
        amenitybase = Amenity()
        self.assertTrue("name" in amenitybase.__dir__())

    def test_Amenityattrtype(self):
        """
        Test Amenity class for attribute type.
        """
        amenitybase = Amenity()
        name_due = getattr(amenitybase, "name")
        self.assertIsInstance(name_due, str)
        