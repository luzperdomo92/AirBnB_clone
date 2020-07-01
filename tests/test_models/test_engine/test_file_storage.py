#!/usr/bin/python3
"""Unittest module for the FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class"""

    def resetStorage(self):
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test instantiation of storage class"""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
            msg = "descriptor '__init__' of 'object' object needs an argument"
            self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
            msg = "object() takes no parameters"
            self.assertEqual(str(e.exception), msg)

    def test_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()
