#!/usr/bin/python3
"""
 Marks directory as a python package
 Sets FileStorage() class to storage
 Calls reload() instance on storage
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
