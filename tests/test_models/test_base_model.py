#!/usr/bin/python3
"""Unittest for BaseModel module"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    """test BaseModel class"""

    def test_creation(self):
        """check if instance is created"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_id_instance(self):
        """check id"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_created_at(self):
        """check created_at attribute"""
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    def test_updated_at(self):
        """check updated_at attribute"""
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)

    def test_save(self):
        """check save method"""
        b1 = BaseModel()
        old_datetime = b1.updated_at
        b1.save()
        new_datetime = b1.updated_at
        self.assertNotEqual(old_datetime, new_datetime)

    def test_to_dict(self):
        """check to_dict method"""
        b1 = BaseModel()
        new_dict = b1.to_dict()
        self.assertIsInstance(new_dict, dict)
    

    if __name__ == "__main__":
            unittest.main()
