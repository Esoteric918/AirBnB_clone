#!/usr/bin/python3
''' Model defines class Place'''

from models.base_model import BaseModel

class Place(BaseModel):
    '''Defining Review inherited from BaseModel'''

    city_id = ""
    user_is = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest: = 0
    price_by_night: = 0
    latitude: = 0.0
    longitude: = 0.0
    amenity_ids = []