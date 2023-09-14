#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    """ Initial class """
    def area(self):
        """ Defining class instance """
        """ raise an exception with message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defining class instance """
        if not isinstance(value, int):
            """ If value is not an integer """
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """ if value is less or equal to 0 """
            raise ValueError(f"{name} must be greater than 0")
