#!/usr/bin/env python3
"""
 a class BaseModel that defines all common attributes/methods for other classes
"""
import models
from datetime import datetime
import uuid

datetime_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel - defines all common attributes/methods for its subclasses.
    """
    def __init__(self, *args, **kwargs):
        """
        initializes instance attribute
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    dic_plat = datetime.strptime(value, datetime_format)
                    self.__dict__[key] = dic_plat
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        save - updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Creates an updated __dict__ containing all keys/values
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """
        str method for BaseModel Class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)
