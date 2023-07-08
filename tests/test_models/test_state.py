#!/usr/bin/python3
"""Unittest for State module"""
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """test State class"""

    def test_creation(self):
        """check if instance is created"""
        s1 = State()
        self.assertIsInstance(s1, State)

    def test_name(self):
        """check name"""
        s1 = State()
        self.assertIsInstance(s1.name, str)
        self.assertEqual(s1.name, "")

    if __name__ == "__main__":
            unittest.main()