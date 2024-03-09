#!/usr/bin/env python3

""" this is the file storage class """

import json
import os


class FileStorage:
    """ make a file storage class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return all objects in the dict """

        return FileStorage.__objects

    def new(self, obj):
        """
            make a new object ready with it class
            name and id as a key

            Args:
                obj: object passed to save in the dict
        """

        pk = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[pk] = obj

    def save(self):
        """ serialize objects and save to a json file """

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            data = {
                key: value.to_dict() for key,
                value in FileStorage.__objects.items()}
            json.dump(data, file)

    def reload(self):
        """ check if json file exist if yes retrieve
        data and return the object """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="utf-8") as file:
                object_dict = json.load(file)
                object_dict = {key: self.classes()[value["__class__"]](**value)
                               for key, value in object_dict.items()}
                FileStorage.__objects = object_dict
        else:
            return

    def classes(self):
        """ return a dict of key value with all
        classed available """
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
