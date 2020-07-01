#!/usr/bin/python3
"""Creating a new class"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Class model "BaseModel" for the entire program """

    def __init__(self, *args, **kwargs):
        """ Constructor for BaseModel"""
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs.get(key),
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Method that returns the string representation of the object"""
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def __repr__(self):
        """f"""
        return '"{}"'.format(self.__str__())

    def save(self):
        """ Method that updates attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method that returns a dictionary
        containing all keys/values of __dict__ of the instance
        """
        new_dic = self.__dict__.copy()
        new_dic['__class__'] = self.__class__.__name__
        new_dic['created_at'] = self.created_at.isoformat()
        new_dic['updated_at'] = self.updated_at.isoformat()
        return new_dic

    def set_attribute(self, attr_name, value):
        """f"""
        setattr(self, attr_name, value)
        self.updated_at = datetime.now()
        models.storage.save()
