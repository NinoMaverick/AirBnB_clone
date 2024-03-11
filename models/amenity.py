#!/usr/bin/python3
"""
 classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class inherits from BaseModel
    it's a public class attribute for Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init method for Amenity class
        """
        super().__init__(*args, **kwargs)
