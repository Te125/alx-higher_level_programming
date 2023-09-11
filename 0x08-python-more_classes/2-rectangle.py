#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
    """ Defines Rectangle Class with attributes """
    def __init__(self, width=0, height=0):
        """ Initial Rectangle Class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter to retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter to set width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter to retrieve """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter to set height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        return 2 * (self.__width + self.__height)
