#!/usr/bin/python3
"""Unittest for Review module"""
import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """test Review class"""

    def test_creation(self):
        """check if instance is created"""
        r1 = Review()
        self.assertIsInstance(r1, Review)

    def test_place_id(self):
        """check place_id"""
        r1 = Review()
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(r1.place_id, "")

    def test_user_id(self):
        """check user_id"""
        r1 = Review()
        self.assertIsInstance(r1.user_id, str)
        self.assertEqual(r1.user_id, "")

    def test_text(self):
        """check text"""
        r1 = Review()
        self.assertIsInstance(r1.text, str)
        self.assertEqual(r1.text, "")

    if __name__ == "__main__":
            unittest.main()