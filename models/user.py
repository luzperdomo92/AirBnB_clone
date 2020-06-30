#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ """
    
    def __init__(self, *args, **kwargs):
        """ """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
