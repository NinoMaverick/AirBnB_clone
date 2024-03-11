#!/usr/bin/python3
"""
importing the Filestorage class from the filestorage module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.deserialize()
