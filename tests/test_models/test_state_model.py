#!/usr/bin/python3
"""
importing modules
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test tate class.
    """

    def test_State_inheritence(self):
        """
        Test state inheritance.
        """
        statebase = State()
        self.assertIsInstance(statebase, BaseModel)

    def test_State_attributes(self):
        """
        Test state attributes
        """
        statebase = State()
        self.assertTrue("name" in statebase.__dir__())

    def test_State_attributes_type(self):
        """
        Test for state attribute type.
        """
        statebase = State()
        name = getattr(statebase, "name")
        self.assertIsInstance(name, str)
        