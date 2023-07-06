#!/usr/bin/pyhton3
import json
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
        key = obj.__class__.__name__ + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize to JSON file"""
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """deserialize the JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                json.loads(f.read())
        except FileNotFoundError:
            pass
