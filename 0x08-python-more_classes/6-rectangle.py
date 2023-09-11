#!/usr/bin/python3
""" Class rectangle """


class Rectangle:
    """ defines rectangle class """
    number_of_instances = 0
    """ Class attribute """

    def __init__(self, width=0, height=0):
        """ Initial class attribute """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter to retrieve """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter to set if int > 0 """
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
        """ Setter to set if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Displays rectangle as string """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """ Displays representation of the object """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Requested message instance when deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
