#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    my_model.save()
    print(my_model)

if __name__ == '__main__':
    unittest.main()
