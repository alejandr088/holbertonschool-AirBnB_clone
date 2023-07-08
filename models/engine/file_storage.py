#!/usr/bin/pyhton3
import json
import os
"""FileStorage module"""


class FileStorage:
    """define FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets items in the __objects dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize to JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserialize the JSON file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity

        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "Review": Review, "Place": Place,
                   "City": City, "Amenity": Amenity}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                content_dict = json.load(f)
                FileStorage.__objects = {}
                for key, value in content_dict.items():
                    class_name = key.split(".")[0]
                    FileStorage.__objects[key] = classes[class_name](**value)
