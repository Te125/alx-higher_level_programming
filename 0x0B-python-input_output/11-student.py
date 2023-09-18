#!/usr/bin/python3
""" class module """


class Student:
    """ class function that defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student """
        if attrs is None:
            """ retrieve if attributes name is in the list """
            return self.__dict__
        else:
            """ otherwise all attributes must be retrieved """
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ replaces all attributes of student instance """
        for key, value in json.items():
            """ loop through the attributes """
            setattr(self, key, value)
