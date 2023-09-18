#!/usr/bin/python3
""" class function """


class Student:
    """ class function that defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ If attrs is None, retrieve all attributes """
        if attrs is None:
            """ return dict """
            return self.__dict__
        """ Initialize an empty dictionary to store the serialized data """
        json_data = {}
        """ Loop through the specified attributes """
        for attr_name in attrs:
            """ Check if the attribute exists in the object's dictionary """
            if attr_name in self.__dict__:
                json_data[attr_name] = self.__dict__[attr_name]

        return json_data
