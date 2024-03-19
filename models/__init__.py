#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

storage = FileStorage()
storage.reload()
