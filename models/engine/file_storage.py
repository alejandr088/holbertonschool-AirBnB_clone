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
        return self.__objects

    def new(self, obj):
        """sets items in the __objects dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize to JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserialize the JSON file"""
        from models.base_model import BaseModel


        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                content_dict = json.load(f)
                self.__objects = {}
                for key, value in content_dict.items():
                    self.__objects[key] = BaseModel(**value)
