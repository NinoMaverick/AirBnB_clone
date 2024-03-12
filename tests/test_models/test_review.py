#!/usr/bin/python3
"""module for testing review class"""
import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import re
import json
import os
from datetime import datetime
import time
from models import storage
import uuid
from models.base_model import BaseModel



class TestReview(unittest.TestCase):

    """
    test class for review
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

    def test_instantiation(self):
        """
        check that an instance is what we want it to be
        """

        base = Review()
        self.assertEqual(str(type(base)), "<class 'models.review.Review'>")
        self.assertIsInstance(base, Review)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attr(self):
        """
        check attribute existence
        """
        base = Review()
        self.assertTrue(base.place_id == "")
        self.assertTrue(base.user_id == "")
        self.assertTrue(base.text == "")


if __name__ == "__main__":
    unittest.main()