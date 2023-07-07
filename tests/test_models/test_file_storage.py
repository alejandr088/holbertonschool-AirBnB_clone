import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        pass

    def test_reload(self):
        # Test reloading when the file exists
        self.storage.reload()
        # Add assertions to verify that the objects were loaded correctly

        # Test reloading when the file doesn't exist
        # Create a temporary file path that doesn't exist
        self.storage._FileStorage__file_path = "nonexistent_file.json"
        self.storage.reload()
        # Add assertions to verify that no objects were loaded

    def test_save(self):
        # Test saving objects to the file
        # Create some objects and add them to the storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        # Read the file and verify its contents using assertions

    def test_new(self):
        # Test adding objects to the storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        # Add assertions to verify that the objects were added correctly

    def test_all(self):
        # Test retrieving all objects from the storage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_objects = self.storage.all()
        # Add assertions to verify that the returned dictionary contains the expected objects

    if __name__ == '__main__':
        unittest.main()
