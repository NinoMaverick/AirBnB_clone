#!/usr/bin/python3s
"""
test for the user model
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Testing Place class
    """

    def setUp(self):
        """
        Creates an instance for place.
        """
        self.newbase = Place()

    def TearDown(self):
        pass

    def test_Place_inheritance(self):
        """
        tests that the City class Inherits from BaseModel
        """

        self.assertIsInstance(self.newbase, BaseModel)

    def test_Place_attributes(self):
        """
        Checks that the attribute exist.
        """
        self.assertTrue("description" in self.newbase.__dir__())
        self.assertTrue("max_guest" in self.newbase.__dir__())
        self.assertTrue("amenity_ids" in self.newbase.__dir__())
        self.assertTrue("number_rooms" in self.newbase.__dir__())
        self.assertTrue("name" in self.newbase.__dir__())
        self.assertTrue("price_by_night" in self.newbase.__dir__())
        self.assertTrue("city_id" in self.newbase.__dir__())
        self.assertTrue("latitude" in self.newbase.__dir__())
        self.assertTrue("longitude" in self.newbase.__dir__())
        self.assertTrue("user_id" in self.newbase.__dir__())


    def test_type_longitude(self):
        """
        Test the type of longitude.
        """
        longitude = getattr(self.newbase, "longitude")
        self.assertIsInstance(longitude, float)

    def test_type_amenity(self):
        """
        Test the type of latitude
        """
        amenity = getattr(self.newbase, "amenity_ids")
        self.assertIsInstance(amenity, list)
    
    def test_type_latitude(self):
        """
        Test the type of latitude
        """
        latitude = getattr(self.newbase, "latitude")
        self.assertIsInstance(latitude, float)

    
    def test_type_price_by_night(self):
        """
        Test the type of price_by_night
        """
        price_by_night = getattr(self.newbase, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_type_max_guest(self):
        """
        Test the type of max_guest
        """
        max_guest = getattr(self.newbase, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_type_number_bathrooms(self):
        """
        Test the type of number_bathrooms
        """
        number_bathrooms = getattr(self.newbase, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_type_number_rooms(self):
        """
        Test the type of number_bathrooms
        """
        number_rooms = getattr(self.newbase, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_type_description(self):
        """
        Test the type of description
        """
        description = getattr(self.newbase, "description")
        self.assertIsInstance(description, str)

    def test_type_city_id(self):
        """
        Test the type of city_id
        """
        city_id = getattr(self.newbase, "city_id")
        self.assertIsInstance(city_id, str)
    
    def test_type_name(self):
        """
        Test the type of name
        """
        name = getattr(self.newbase, "name")
        self.assertIsInstance(name, str)

    def test_type_user_id(self):
        """
        Test the type of user_id
        """
        user_id = getattr(self.newbase, "user_id")
        self.assertIsInstance(user_id, str)
