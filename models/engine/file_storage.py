#!/usr/bin/python3

import json
import os


class FileStorage:
    """ make a file storage class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return all objects in the dict """

        return self.__objects

    def new(self, obj):
        """
            make a new object ready with it class
            name and id as a key

            Args:
                obj: object passed to save in the dict
        """

        pk = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[pk] = obj

    def save(self):
        """ serialize objects and save to a json file """

        with open(self.__file_path, 'w') as file:
            data = {
                key: value.to_dict() for key,
                value in self.__objects.items()}
            json.dump(data, file, indent=4)

    def reload(self):
        """ check if json file exist if yes retrieve
        data and return the object """

        if os.path.exists(self.__file_path):
            with open(self.__file_path) as file:
                obj_dict = json.load(file)
                return obj_dict

    def classes(self):
        from models.base_model import BaseModel
        from models. user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
        }

        return classes_dict
