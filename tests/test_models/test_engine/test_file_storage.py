#!/usr/bin/python3
"""Unittest for file_storage module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test FileStorage class"""

    def test_file_path(self):
        """check __file_path attribute"""
        fs = FileStorage()
        self.assertEqual(fs._FileStorage__file_path, "file.json")

    def test_objects(self):
        """check __objects attribute"""
        fs = FileStorage()
        self.assertIsInstance(fs._FileStorage__objects, dict)

    def test_all(self):
        """check all method"""
        fs = FileStorage()
        all_dict = fs.all()
        self.assertIsInstance(all_dict, dict)
        self.assertNotEqual(all_dict, {})

    def test_new(self):
        """check new method"""
        fs = FileStorage()
        add_base = BaseModel()
        fs.new(add_base)
        self.assertNotEqual(fs._FileStorage__objects, {})

    def test_save(self):
        """check save method"""
        fs = FileStorage()
        all_dict = fs.all()
        add_base = BaseModel()
        fs.save()
        self.assertNotEqual(all_dict, {})

    def test_reload(self):
        """check reload method"""
        fs = FileStorage()
        all_dict = fs.all()
        fs.reload()
        self.assertNotEqual(all_dict, {})

    if __name__ == '__main__':
        unittest.main()