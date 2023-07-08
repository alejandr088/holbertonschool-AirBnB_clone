#!/usr/bin/python3
"""Unittest for User module"""
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """test User class"""

    def test_creation(self):
        """check if instance is created"""
        u1 = User()
        self.assertIsInstance(u1, User)

    def test_email(self):
        """check email"""
        u1 = User()
        self.assertIsInstance(u1.email, str)
        self.assertEqual(u1.email, "")

    def test_password(self):
        """check password"""
        u1 = User()
        self.assertIsInstance(u1.password, str)
        self.assertEqual(u1.password, "")

    def test_first_name(self):
        """check first_name"""
        u1 = User()
        self.assertIsInstance(u1.first_name, str)
        self.assertEqual(u1.first_name, "")

    def test_last_name(self):
        """check last_name"""
        u1 = User()
        self.assertIsInstance(u1.last_name, str)
        self.assertEqual(u1.last_name, "")

    if __name__ == "__main__":
            unittest.main()