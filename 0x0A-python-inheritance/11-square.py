#!/usr/bin/python3
""" Class that inherits from another """


class BaseGeometry:
    """ Initial class """
    def area(self):
        """ Raise an exception with message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defining class """
        if not isinstance(value, int):
            """ if value is not an integer """
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            """ If value is less or equal to 0 """
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Defining class with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate and return the area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ String representation of the object """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Class square """
    def __init__(self, size):
        """ Define initial class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ String representation """
        return f"[Square] {self.__size}/{self.__size}"
