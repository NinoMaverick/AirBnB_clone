#!/usr/bin/python3
"""
classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """
        init method for City class
        """
        super().__init__(*args, **kwargs)
