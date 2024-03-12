#!/usr/bin/python3
"""
importing modules
"""

from datetime import datetime
from models.state import State
import unittest
import re
import time
import json
import os
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import uuid


class TestState(unittest.TestCase):

    """
    class for tests for state
    """

    def setUp(self):
        """
        set up"""
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
        test instance
        """

        base = State()
        self.assertEqual(str(type(base)), "<class 'models.state.State'>")
        self.assertIsInstance(base, State)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_attr(self):
        """
        testing
        """
        base = State()
        self.assertTrue(base.name == "")


if __name__ == "__main__":
    unittest.main()
    