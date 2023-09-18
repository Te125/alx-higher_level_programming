#!/usr/bin/python3
""" class that defines a student """


class Student:
    """ class definition """
    def __init___(self, first_name, last_name, age):
        """ Initial function definition """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function definition that retrieves a dictionary
        representation of student instance """
        return self.__dict__
