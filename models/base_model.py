#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
"""BaseModel module"""


class BaseModel:
    """define BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialize class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            FileStorage.new(storage)

    def __str__(self):
        """print string"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        instance_dict = self.__dict__
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict
