#!/usr/bin/python3
"""
unittest for BaseModel Class
"""
import os
import time
import re
import uuid
import unittest
import json
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    """
    tests for the BaseModel class
    """
    def setUp(self):
        """
        set up
        """
        pass

    def tearDown(self):
        """
        to tear it all down
        """
        self.resetStorage()
        pass

    def resetStorage(self):
        """
        reset storage
        """
        FileStorage._Filestorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save(self):
        """
        save method testing
        """
        base = BaseModel()
        time.sleep(0.5)
        base.save()
        self.assertTrue(abs(base.updated_at > base.created_at))


    def test_to_dict(self):
        """
        test to_dict
        """
        base = BaseModel()
        base.name = "Gogo"
        base.age = 25
        dic = base.to_dict()
        self.assertEqual(dic["created_at"], base.created_at.isoformat())
        self.assertEqual(dic["name"], base.name)
        self.assertEqual(dic["__class__"], type(base).__name__)
        self.assertEqual(dic["updated_at"], base.updated_at.isoformat())
        self.assertEqual(dic["id"], base.id)
        self.assertEqual(dic["age"], base.age)


        """
        Tests for instantiation
        """
    def test_instance(self):
        """
        test instance
        """

        base = BaseModel()
        string = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(base)), string)
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_init_no_args(self):
        """
        init no args
        """
        with self.assertRaises(TypeError) as v:
            BaseModel.__init__()
        errormsg = """BaseModel.__init__() missing 1 required
        positional argument: 'self'"""
        self.assertEqual(str(v.exception), errormsg)

    def test_datetime_creation(self):
        """
        checking for datetime function
        """
        base = BaseModel()
        date = datetime.now()
        difference = base.updated_at - base.created_at
        self.assertTrue(abs(difference.total_seconds()) < 0.01)
        difference = base.created_at - date
        self.assertTrue(abs(difference.total_seconds()) < 0.1)
    def test_ids_special(self):
        
        """
        test for unique ids
        """
        base = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(base)), len(base))

    def test_save(self):
        """
        save test
        """
        base = BaseModel()
        time.sleep(0.5)
        date = datetime.now()
        base.save()
        self.assertTrue(abs(base.updated_at > base.created_at))

    def test_save_time(self):
        """
        test save time
        """
        base = BaseModel()
        the_time = base.updated_at
        time.sleep(0.001)
        base.save()

        self.assertNotEqual(the_time, base.updated_at)

        with open("file.json", "r") as f:
            self.assertIn(base.to_dict(), json.loads(f.read()).values())

    def test_str_method(self):
        """
        test the str method
        """
        base = BaseModel()
        basin = "[{}] ({}) {}".format("BaseModel",
                                        base.id, base.__dict__)
        self.assertEqual(base.__str__(), basin)

    def test_attr(self):
        """
        test attr
        """
        base = BaseModel()
        self.assertTrue(isinstance(base.id, str))
        self.assertTrue(isinstance(base.created_at, datetime))
        self.assertTrue(isinstance(base.updated_at, datetime))
if __name__ == '__main__':
    unittest.main()
