#!/usr/bin/python3

'''
importing modules
'''

import sys
import unittest
import datetime
from models.user import User
from io import StringIO
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test User class
    """

    def test_User_inheritance(self):
        """
        test User class Inheriting from BaseModel
        """
        userbase = User()
        self.assertIsInstance(userbase, BaseModel)

    def test_User_attributes(self):
        """
        Test the user attributes exis
        """

        userbase = User()
        self.assertTrue("email" in userbase.__dir__())
        self.assertTrue("first_name" in userbase.__dir__())
        self.assertTrue("last_name" in userbase.__dir__())
        self.assertTrue("password" in userbase.__dir__())

    def test_type_email(self):
        """
        Test the type of name
        """
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        """
        Test the type of name
        """
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        """
        Test the type of last_name
        """
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        """
        Test the type of password
        """
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
