#!/usr/bin/python3
""" test module for our FileStorage class"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os
import uuid


class TestFileStorage(unittest.TestCase):
    """
    tests for the FileStorage class
    """

    def setUp(self):
        """
        set up
        """
        pass

    def resetStorage(self):
        """
        reset storage
        """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """
        teardown method
        """
        self.resetStorage()
        pass
    """========================"""

    def test_storage_class(self):
        """
        storage class
        """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_no_args(self):
        """
        test with no args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.__init__()
        error_msg = """descriptor '__init__' of
        'object' object needs an argument"""
        self.assertEqual(str(v.exception), error_msg)

    def test_without_args(self):
        """
        takes args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            base = FileStorage(0, 1, 2, 3, 4)
        error_msg = "FileStorage() takes no arguments"
        self.assertEqual(str(v.exception), error_msg)

    def test_class_attributes(self):
        """
        class attributes
        """
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    """========================"""
    def test_all(self, classname):
        """
        test all() method
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        base = storage.classes()[classname]()
        storage.new(base)
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], base)

    def test_basemodel(self):
        """
        all() BaseModel
        """
        self.test_all("BaseModel")

    def test_user(self):
        """
        method User
        """
        self.test_all("User")

    def test_state(self):
        """
        State
        """
        self.test_all("State")

    def test_all_city(self):
        """
        City
        """
        self.test_all("City")

    def test_amenity(self):
        """
        test all Amenity
        """
        self.test_all("Amenity")

    def test_place(self):
        """
        test for all Place
        """
        self.test_all("Place")

    def test_review(self):
        """
        test all Review
        """

        self.test_all("Review")

    """========================="""

    def test_all_multiple(self, members):
        """
        test multiple objects
        """
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[members]
        obj = [cls() for i in range(1000)]
        [storage.new(thing) for thing in obj]
        self.assertEqual(len(obj), len(storage.all()))
        for thing in obj:
            key = "{}.{}".format(type(thing).__name__, thing.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], thing)

    def test_all_base_model(self):
        """
        test all multiple of Basemodel
        """
        self.test_all_multiple("BaseModel")

    def test_multiiple_user(self):
        """
        all() for user
        """
        self.test_all_multiple("User")

    def test_all_multi_state(self):
        """
        all_multiple() for state
        """
        self.test_all_multiple("State")

    def test_all_multi_city(self):
        """
        all_multiple() for city
        """
        self.test_all_multiple("City")

    def test_all_multi_amenity(self):
        """
        all_multiple() for amenity
        """
        self.test_all_multiple("Amenity")

    def test_all_multi_place(self):
        """
        all_multiple() for place
        """
        self.test_all_multiple("Place")

    def test_all_multi_review(self):
        """
        all_multiple() for review
        """
        self.test_all_multiple("Review")

    def test_all_no_args(self):
        """
        no args please
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.all()
        errormsg = """FileStorage.all() missing 1
        required positional argument: 'self'"""
        self.assertEqual(str(v.exception), errormsg)

    def test_all_such_args(self):
        """
        that's too many
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.all(self, 98)
        errormsg = """FileStorage.all() takes 1
        positional argument but 2 were given"""
        self.assertEqual(str(v.exception), errormsg)

    """==========================="""
    def tool_test_new(self, members):
        """
        new() testing helper
        """
        self.resetStorage()
        cls = storage.classes()[members]
        base = cls()
        storage.new(base)
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], base)

    def test_new_base(self):
        """
        new() test on BaseModel
        """
        self.tool_test_new("BaseModel")

    def test_new_user(self):
        """
        new() test on User
        """
        self.tool_test_new("User")

    def test_new_state(self):
        """
        new() test on state
        """
        self.tool_test_new("State")

    def test_new_city(self):
        """
        new() test on city
        """
        self.tool_test_new("City")

    def test_new_amenity(self):
        """
        new() test on Amenity
        """
        self.tool_test_new("Amenity")

    def test_new_place(self):
        """
        new() test on place
        """
        self.tool_test_new("Place")

    def test_new_review(self):
        """
        new() test on review
        """
        self.tool_test_new("Review")

    def test_new_no_args(self):
        """
        no args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            storage.new()
        errormsg = """FileStorage.new() missing 1
        required positional argument: 'obj'"""
        self.assertEqual(str(v.exception), errormsg)

    def test_new_such_args(self):
        """
        new args
        """
        self.resetStorage()
        base = BaseModel()
        with self.assertRaises(TypeError) as v:
            storage.new(base, 50)
        errormsg = """FileStorage.new() takes 2
        positional arguments but 3 were given"""
        self.assertEqual(str(v.exception), errormsg)

    """==========================="""

    def tool_test_save(self, members):
        """
        helper func for save tests
        """
        self.resetStorage()
        cls = storage.classes()[members]
        obj = cls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        dick = {key: obj.to_dict()}
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(dick)))
            f.seek(0)
            self.assertEqual(json.load(f), dick)

    def test_save_base(self):
        """
        save() a base model test
        """
        self.tool_test_save("BaseModel")

    def test_save_user(self):
        """
        test save for user
        """
        self.tool_test_save("User")

    def test_save_state(self):
        """
        test save for state
        """
        self.tool_test_save("State")

    def test_save_city(self):
        """
        test save for city
        """
        self.tool_test_save("City")

    def test_save_amenity(self):
        """
        test save for amenity
        """
        self.tool_test_save("Amenity")

    def test_save_place(self):
        """
        test save for place
        """
        self.tool_test_save("Place")

    def test_save_review(self):
        """
        tests save for review
        """
        self.tool_test_save("Review")

    def test_save_no_args(self):
        """
        no args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.save()
        errormsg = """FileStorage.save() missing 1
        required positional argument: 'self'"""
        self.assertEqual(str(v.exception), errormsg)

    def test_save_such_args(self):
        """
        such args much wow
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.save(self, 98)
        errormsg = """FileStorage.save() takes 1
        positional argument but 2 were given"""
        self.assertEqual(str(v.exception), errormsg)

    """==========================="""
    def tool_test_reload(self, members):
        """
        a tool to help test reloading
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        cls = storage.classes()[members]
        obj = cls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        storage.reload()
        self.assertEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_reload_base(self):
        """
        test reloading base
        """
        self.tool_test_reload("BaseModel")

    def test_reload_user(self):
        """
        test reload user
        """
        self.tool_test_reload("User")

    def test_reload_state(self):
        """
        test reload state
        """
        self.tool_test_reload("State")

    def test_reload_city(self):
        """
        test reload city
        """
        self.tool_test_reload("City")

    def test_reload_amenity(self):
        """
        test reload amenity
        """
        self.tool_test_reload("Amenity")

    def test_reload_place(self):
        """
        test reload place
        """
        self.tool_test_reload("Place")

    def test_reload_review(self):
        """
        test reload review
        """
        self.tool_test_reload("Review")

    """========================="""
    def tool_test_re_miss(self, members):
        """ 
        tool to test reload
        """
        self.resetStorage()
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})

        cls = storage.classes()[members]
        obj = cls()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        storage.save()
        obj.name = "labrat"
        storage.reload()
        self.assertNotEqual(obj.to_dict(), storage.all()[key].to_dict())

    def test_remiss_base(self):
        """
        test remiss base
        """
        self.tool_test_re_miss("BaseModel")

    def test_remiss_user(self):
        """
        test remiss use
        """
        self.tool_test_re_miss("User")

    def test_remiss_state(self):
        """
        test remiss state
        """
        self.tool_test_re_miss("State")

    def test_remiss_city(self):
        """
        test remiss city
        """
        self.tool_test_re_miss("City")

    def test_remiss_amenity(self):
        """
        test remiss amenity
        """
        self.tool_test_re_miss("Amenity")

    def test_remiss_place(self):
        """
        test reiss place
        """
        self.tool_test_re_miss("Place")

    def test_remiss_review(self):
        """
        test remiss review
        """
        self.tool_test_re_miss("Review")

    def test_reload_no_args(self):
        """
        no args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.reload()
        errormsg = """FileStorage.reload() missing
        1 required positional argument: 'self'"""
        self.assertEqual(str(v.exception), errormsg)

    def test_reload_such_args(self):
        """
        such args
        """
        self.resetStorage()
        with self.assertRaises(TypeError) as v:
            FileStorage.reload(self, 98)
        errormsg = """FileStorage.reload() takes
        1 positional argument but 2 were given"""
        self.assertEqual(str(v.exception), errormsg)


if __name__ == '__main__':
    unittest.main()
