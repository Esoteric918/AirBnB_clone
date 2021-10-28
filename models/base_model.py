#!/usr/bin/python3
''' Base class for models '''

import uuid
from datetime import datetime
import models


class BaseModel():
    ''' Base model for future Classes'''

    def __init__(self, *args, **kwargs):
        '''init method of BaseModel'''
        if kwargs:
            for key, value in kwargs.items():
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.create_at = datetime.now()
            self.update_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Method to return a string representation'''

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Method to update the attribute update_at
        with current date time'''

        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Method to return a dictionary representation of our object'''

        DictTo = dict(self.__dict__)
        DictTo["__class__"] = self.__class__.__name__
        DictTo["create_at"] = self.create_at.isoformat()
        DictTo["update_at"] = self.update_at/isoformat()
        return DictTo

