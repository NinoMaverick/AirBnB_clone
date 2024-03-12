#!/usr/bin/python3
"""
tests module for Amenity class
"""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestAmenity(unittest.TestCase):

    """
    test class for amenity
    """

    def setUp(self):
        """
        set it up
        """
        pass

    def tearDown(self):
        """
        tear down
        """
        self.resetStorage()
        pass
    
    def test_attributes(self):
        """ test existence of attributes"""
        base = Amenity()
        self.assertTrue(base.name == "")

    def resetStorage(self):
        """
        reset storage
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def test_instance(self):
        """
        instance of the class
        """

        base = Amenity()
        self.assertEqual(str(type(base)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(base, Amenity)
        self.assertTrue(issubclass(type(base), BaseModel))



if __name__ == "__main__":
    unittest.main()
    