#!/usr/bin/python3
""" class module """
import json
import os


class Base:
    """Base class for managing id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): optional integer ID for the instance.
        """
        if id is not None:
            """ assign the public instance attrinute id if it is none """
            self.id = id
        else:
            """ otherwise increment nb_objects and assign new value """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that returns the json string representation """
        if not list_dictionaries:
            return "[]"
        """ return the list """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes the json representation of a list """
        if list_objs is None:
            """ if obj is none, save an empty list """
            list_objs = []

        filename = "{}.json".format(cls.__name__)

        """ Check if the file exists """
        if not os.path.exists(filename):
            """ if file does not exixts, create an empty file """
            with open(filename, 'w') as file:
                file.write("[]")
        with open(filename, 'w') as file:
            """ overwrite file if it already exists """
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string)

        Base.__nb_objects = 0

    @staticmethod
    def from_json_string(json_string):
        """ Method that parses a json string representation into a list """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ method that returns an instance with all attributes """
        print("Creating with class:", cls.__name__)
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
            """ assign all attributes with dummy instance """
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            return None
        """ Update the instance attributes using provided dictionary """
        dummy_instance.update(**dictionary)

        return dummy_instance

    def update(self, *args, **kwargs):
        """ Method to update dictionary """
        if args:
            attrs = ["id", "width", "height", "x", "y"] if cls.__name__ == 'Rectangle' else ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ create an update to dictionary """
        attrs = ["id", "width", "height", "x", "y"] if cls.__name__ == 'Rectangle' else ["id", "size", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
