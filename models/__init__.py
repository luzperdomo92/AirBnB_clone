#!/usr/bin/python3
""" Storage file"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
