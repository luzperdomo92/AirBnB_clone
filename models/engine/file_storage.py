#!/usr/bin/python3
"""FileStorage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class for serializtion and deserialization of base classes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialzes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes JSON file into __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as f:
                jo = json.load(f)
            for k, v in jo.items():
                FileStorage.__objects[k] = BaseModel(**v)
