#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """r"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """d"""
        super().__init__(*args, **kwargs)
