#!/usr/bin/python3
"""Creating a new class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """p"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """d"""
        super().__init__(*args, **kwargs)

    def set_attribute(self, attr_name, value):
        """d"""
        if attr_name in ("number_rooms", "number_bathrooms", "max_guest",
                         "price_by_night"):
            value = int(value)
        elif attr_name in ("latitude", "longitude"):
            value = float(value)

        super().set_attribute(attr_name, value)
