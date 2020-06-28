#!/usr/bin/python3
"""Unittest for base_model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class testBaseModelClass(unittest.TestCase):
      """Test for class BaseModel"""
      def test_instantiation(self):
              """Test instantiation"""
              b = BaseModel()
              self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
              self.assertIsInstance(b, BaseModel)
              self.assertTrue(issubclass(type(b), BaseModel))

      def test_datatime_created(self):
            """Test if updated_at & created_at are current at creation"""
            date_now = datetime.now()
            b = BaseModel()
            diff = b.updated_at - b.created_at
            self.assertTrue(abs(diff.total_seconds()) < 0.1)
            diff = b.created_at - date_now
            self.assertTrue(abs(diff.total_seconds()) < 0.1)

      def test_id(self):
            """Test for unique user ids"""
            l = [BaseModel().id for i in range(1000)]
            self.assertEqual(len(set(l)), len(l))

      def test_to_dict(self):
            """Tests the public instance method to_dict()."""
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
            """test that the str method has the correct output"""
            b = BaseModel()
            string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
            self.assertEqual(string, str(b))

if __name__ == "__main__":
        unittest.main()
