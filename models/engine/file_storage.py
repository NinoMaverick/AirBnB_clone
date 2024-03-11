#!/usr/bin/env python3
"""
Filestorage BaseModel that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
from datetime import datetime
import json


class FileStorage:
    """
    FileStorage BaseModel that serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        function that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def serialize(self):
        """
        save - serializes __objects to a JSON file (path: __file_path)
        """
        file_dict = {key: value.to_dict() for key, value in
                     FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(file_dict, file)

    def classes(self):
        """
        Returns a dict of all valid classes
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review,
                   "User": User}
        return classes

    def deserialize(self):
        """
        deserializes a JSON file to __objects only if the JASON file
        exists, otherwise raise an exeption ltion that does nothing but return.
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json_file = json.load(file)
            json_file = {k: self.classes()[v["__class__"]](**v) for k, v in
                         json_file.items()}
            FileStorage.__objects = json_file
        except:
            pass