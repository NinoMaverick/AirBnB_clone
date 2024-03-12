#!/usr/bin/python3
"""
test module for city class
"""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestCity(unittest.TestCase):

    """tests for ye olde City"""

    def setUp(self):
        """
        set up
        """
        pass

    def tearDown(self):
        """
        tear it all down
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """
        test for instance
        """

        base = City()
        self.assertEqual(str(type(base)), "<class 'models.city.City'>")
        self.assertIsInstance(base, City)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attributes(self):
        """
        test attributes of the city class
        """
        base = City()
        self.assertTrue(base.state_id == "")
        self.assertTrue(base.name == "")


if __name__ == "__main__":
    unittest.main()