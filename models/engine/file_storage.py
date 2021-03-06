#!/usr/bin/python3
"""FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for serializtion and deserialization of base classes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary"""
        FileStorage.__objects[self.obj_key(obj)] = obj

    def save(self):
        """Serialzes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes JSON file into __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r') as f:
                try:
                    jo = json.load(f)
                except json.decoder.JSONDecodeError:
                    jo = {}

            for k, v in jo.items():
                class_name = k.split('.')[0]
                if class_name == 'User':
                    instance = User(**v)
                elif class_name == "State":
                    instance = State(**v)
                elif class_name == "City":
                    instance = City(**v)
                elif class_name == "Amenity":
                    instance = Amenity(**v)
                elif class_name == "Place":
                    instance = Place(**v)
                elif class_name == "Review":
                    instance = Review(**v)
                else:
                    instance = BaseModel(**v)
                FileStorage.__objects[k] = instance

    def find(self, class_name, id):
        """ Method to find all element in the __objects """
        try:
            return self.all()["{}.{}".format(class_name, id)]
        except KeyError:
            None

    def destroy(self, obj):
        """d"""
        del self.all()[self.obj_key(obj)]
        self.save()

    def obj_key(self, obj):
        """d"""
        return "{}.{}".format(type(obj).__name__, obj.id)

    def filter_by_class_name(self, class_name):
        """d"""
        return(
            dict(
                filter(
                    lambda key_value:
                        class_name == key_value[1].__class__.__name__,
                        self.all().items()
                )
            )
        )
