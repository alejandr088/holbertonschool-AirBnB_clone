#!/usr/bin/pyhton3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"""
    pass

    def test_id(self):
        """"""
        a1 = BaseModel() 
        
        self.assertEqual(a1.id)
