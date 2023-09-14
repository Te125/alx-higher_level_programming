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
    """ Rectangle class """
    def __init__(self, width, height):
        """ Define class with width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
