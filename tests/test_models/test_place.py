#!/usr/bin/python3

"""
test for the user model.
"""

from models.base_model import BaseModel
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """
    Testing User class
    """


    def test_User_attributes(self):
        citybase = City()
        self.assertTrue("state_id" in citybase.__dir__())
        self.assertTrue("name" in citybase.__dir__())

    def test_City_inheritance(self):
        """
        tests that the City class Inherits from BaseModel
        """
        citybase = City()
        self.assertIsInstance(citybase, BaseModel)

    def test_name(self):
        """
        Test the type of name
        """
        new_city = City()
        name = getattr(new_city, "state_id")
        self.assertIsInstance(name, str)

    def test_name(self):
        """
        Test the type of name
        """
        citybase = City()
        name = getattr(citybase, "name")
        self.assertIsInstance(name, str)
        