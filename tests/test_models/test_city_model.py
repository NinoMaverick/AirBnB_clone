#!/usr/bin/python3

"""
test for the user model.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Testing User class
    """

    def test_City_inheritance(self):
        """
        tests city inheritance
        """
        citybase = City()
        self.assertIsInstance(citybase, BaseModel)


    def test_type_name(self):
        """
        Test the type of name
        """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_User_attributes(self):
        citybase = City()
        self.assertTrue("state_id" in citybase.__dir__())
        self.assertTrue("name" in citybase.__dir__())

    def test_type_name(self):
        """
        Test the type of name
        """
        citybase = City()
        name = getattr(citybase, "state_id")
        self.assertIsInstance(name, str)
