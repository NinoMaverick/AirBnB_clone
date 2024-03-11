#!/usr/bin/python3
"""module to test the console/ TestCommand"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os

class TestCommand(unittest.TestCase):
     
     def test_quit(self):
        """
        test for quit
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

if __name__ == "__main__":
    unittest.main()