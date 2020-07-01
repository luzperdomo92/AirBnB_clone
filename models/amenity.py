#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a"""
    name = ""

    def __init__(self, *args, **kwargs):
        """d"""
        super().__init__(*args, **kwargs)
