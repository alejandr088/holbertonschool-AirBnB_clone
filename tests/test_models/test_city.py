#!/usr/bin/python3
"""Unittest for City module"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """test City class"""

    def test_creation(self):
        """check if instance is created"""
        c1 = City()
        self.assertIsInstance(c1, City)

    def test_state_id(self):
        """check state_id"""
        c1 = City()
        self.assertIsInstance(c1.state_id, str)
        self.assertEqual(c1.state_id, "")

    def test_name(self):
        """check name"""
        c1 = City()
        self.assertIsInstance(c1.name, str)
        self.assertEqual(c1.name, "")

    if __name__ == "__main__":
            unittest.main()