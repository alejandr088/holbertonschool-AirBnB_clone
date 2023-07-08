#!/usr/bin/python3
"""Unittest for Place module"""
import unittest
from models.place import Place


class test_Place(unittest.TestCase):
    """test Place class"""

    def test_creation(self):
        """check if instance is created"""
        p1 = Place()
        self.assertIsInstance(p1, Place)

    def test_city_id(self):
        """check city_id"""
        p1 = Place()
        self.assertIsInstance(p1.city_id, str)
        self.assertEqual(p1.city_id, "")

    def test_user_id(self):
        """check user_id"""
        p1 = Place()
        self.assertIsInstance(p1.user_id, str)
        self.assertEqual(p1.user_id, "")

    def test_name(self):
        """check name"""
        p1 = Place()
        self.assertIsInstance(p1.name, str)
        self.assertEqual(p1.name, "")

    def test_description(self):
        """check description"""
        p1 = Place()
        self.assertIsInstance(p1.description, str)
        self.assertEqual(p1.description, "")

    def test_number_rooms(self):
        """check number_rooms"""
        p1 = Place()
        self.assertIsInstance(p1.number_rooms, int)
        self.assertEqual(p1.number_rooms, 0)

    def test_number_bathrooms(self):
        """check number_bathrooms"""
        p1 = Place()
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertEqual(p1.number_bathrooms, 0)

    def test_max_guest(self):
        """check max_guest"""
        p1 = Place()
        self.assertIsInstance(p1.max_guest, int)
        self.assertEqual(p1.max_guest, 0)

    def test_price_by_night(self):
        """check price_by_night"""
        p1 = Place()
        self.assertIsInstance(p1.price_by_night, int)
        self.assertEqual(p1.price_by_night, 0)

    def test_latitude(self):
        """check latitude"""
        p1 = Place()
        self.assertIsInstance(p1.latitude, float)
        self.assertEqual(p1.latitude, 0.0)

    def test_longitude(self):
        """check longitude"""
        p1 = Place()
        self.assertIsInstance(p1.longitude, float)
        self.assertEqual(p1.longitude, 0.0)

    def test_amenity_ids(self):
        """check amenity_id"""
        p1 = Place()
        self.assertIsInstance(p1.amenity_ids, list)
        self.assertEqual(p1.amenity_ids, [])

    if __name__ == "__main__":
            unittest.main()