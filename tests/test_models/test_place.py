#!/usr/bin/python3
"""
importing modules
"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestPlace(unittest.TestCase):

    """
    class tests for Place class
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
        """
        reset storage
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instance(self):
        """
        test instance
        """

        base = Place()
        self.assertEqual(str(type(base)), "<class 'models.place.Place'>")
        self.assertIsInstance(base, Place)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attr(self):
        """check the attributes exist"""
        base = Place()
        self.assertTrue(base.user_id == "")
        self.assertTrue(base.name == "")
        self.assertTrue(base.city_id == "")
        self.assertTrue(base.description == "")
        self.assertTrue(base.price_by_night == 0)
        self.assertTrue(base.number_rooms == 0)
        self.assertTrue(base.max_guest == 0)
        self.assertTrue(base.latitude == 0.0)
        self.assertTrue(base.amenity_ids == [])
        self.assertTrue(base.number_bathrooms == 0)
        self.assertTrue(base.longitude == 0.0)


if __name__ == "__main__":
    unittest.main()