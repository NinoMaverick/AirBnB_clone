#!/usr/bin/python3
"""
 class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel

    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        init method for User class
        """
        super().__init__(*args, **kwargs)
