#!/usr/bin/python3
"""Unittest module for the State Class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test Cases for the State class"""
    def test_instantiation(self):
        """Tests instantiation of State class."""
        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_name_attr(self):
        """Tests that State attribute name, and it's as an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()
