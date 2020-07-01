#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class User(BaseModel):
    """u"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """d"""
        super().__init__(*args, **kwargs)
