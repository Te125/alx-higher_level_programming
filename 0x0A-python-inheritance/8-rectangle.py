#!/usr/bin/python3
""" Class BaseGeometry """


class BaseGeometry:
    """ Initial class """
    def area(self):
        """ Raises an exception with message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defining class """
        if not isinstance(value, int):
            """ if value is not an intege """
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """ if value is less or equal to 0 """
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Instantation with width and height """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
