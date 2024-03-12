#!/usr/bin/python3
"""
importing modules
"""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestUser(unittest.TestCase):

    """
    class test
    """

    def setUp(self):
        """
        set up
        """
        pass

    def tearDown(self):
        """
        tear down
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


    def test_attr(self):
        """
        test for atttributes
        """
        base = User()
        self.assertTrue(base.password == "")
        self.assertTrue(base.email == "")
        self.assertTrue(base.last_name == "")
        self.assertTrue(base.first_name == "")
   
    def test_instance(self):
        """
        test for instance
        """

        base = User()
        self.assertIsInstance(base, User)
        self.assertTrue(issubclass(type(base), BaseModel))
        self.assertEqual(str(type(base)), "<class 'models.user.User'>")


if __name__ == "__main__":
    unittest.main()