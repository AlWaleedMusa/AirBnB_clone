#!/usr/bin/env python3

""" This is the base model for my hbnb project """

import datetime
import uuid
from models import storage


class BaseModel:
    """ creating a base model """

    def __init__(self, *args, **kwargs):
        """
            initializing model with uniq id, and
            created at, updated time timestamp
            if **kwargs is not provided else make
            a model of the provided data

            Args:
                *args: arguments passed to the class
                **kwargs: key, value passed to the class
        """

        if kwargs and kwargs != {}:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    if isinstance(value, str):
                        setattr(
                            self,
                            key,
                            datetime.datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ return a string representation of the instance """

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """ update the instance 'update_at'
        attribute to the current time """

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """return a copy version of __dict__ with
        the class name and convert dates to ISO format """

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
