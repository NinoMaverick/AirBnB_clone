#!/usr/bin/python3
"""
Public class attributes
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class attributes inherits from BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init method for State class
        """
        super().__init__(*args, **kwargs)
