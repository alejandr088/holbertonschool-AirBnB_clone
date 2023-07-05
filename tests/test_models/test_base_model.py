#!/usr/bin/python3
"""Unittest for BaseModel class"""
from models.base_model import BaseModel
import unittest


class TestBase(unittest.TestCase):
    """test methods from BaseModel class"""
    
    def test_base_attributes(self):
        """test if new attributes are created correctly"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        self.assertEqual(my_model.name, 'My First Model')
    
if __name__ == "__main__":
    unittest.main()
