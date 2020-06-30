#!/usr/bin/python3
"""Unittest for base_model"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import pep8
import os


class testBaseModelClass(unittest.TestCase):
    """a"""
    def test_module_docstring(self):
        """b"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def resetStorage(self):
        """c"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_class_doc(self):
        """d"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_functions_docs(self):
        """e"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_instantiation(self):
        """f"""
        b = BaseModel()
        self.assertEqual(str(type(b)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_pep8(self):
        """g"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base_model.py'
        file2 = 'tests/test_models/test_base_model.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

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
