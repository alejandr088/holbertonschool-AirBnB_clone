#!/usr/bin/python3
"""Unittest for Amenity module"""
import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """test Amenity class"""

    def test_creation(self):
        """check if instance is created"""
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)

    def test_name(self):
        """check name"""
        a1 = Amenity()
        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, "")

    if __name__ == "__main__":
            unittest.main()