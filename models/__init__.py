#!/usr/bin/python3
"""create a unique FileStorage insatnce"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
FileStorage.reload(storage)
