#!/usr/bin/python3
"""Unittest for base_model"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import time
import os


class testBaseModelClass(unittest.TestCase):
    """a"""
    def resetStorage(self):
        """c"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """f"""
        b = BaseModel()
        self.assertEqual(str(type(b)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_init_no_args(self):
        """h"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """i"""
        self.resetStorage()
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = BaseModel(*args)

    def test_datatime_created(self):
        """j"""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.1)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        """k"""
        l = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(l)), len(l))

    def test_3_save(self):
        """n"""
        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_to_dict(self):
        """l"""
        b = BaseModel()
        b.name = "Adonis"
        b.age = 22
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["name"], b.name)
        self.assertEqual(d["age"], b.age)

    def test_str(self):
        """m"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

if __name__ == "__main__":
        unittest.main()
