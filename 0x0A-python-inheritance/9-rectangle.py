#!/usr/bin/python3
""" rectangle that inherits from BaseGeometry """


class BaseGeometry:
    """ Initial class """
    def area(self):
        """ Defining class """
        """ raise exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defining class """
        if not isinstance(value, int):
            """ If value is not an integer """
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """ If value is less or equal to 0 """
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Class wth width and height """
    def __init__(self, width, height):
        """ Defining class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of the object """
        return f"[Rectangle] {self.__width}/{self.__height}"
