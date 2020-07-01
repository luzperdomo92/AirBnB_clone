#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class State(BaseModel):
    """s"""
    name = ""

    def __init__(self, *args, **kwargs):
        """d"""
        super().__init__(*args, **kwargs)
