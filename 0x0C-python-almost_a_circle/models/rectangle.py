#!/usr/bin/python3
""" Defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initial rectangle class.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
            x (int): X-coordinate of rectangle position (default is 0).
            y (int): Y-coordinate of rectangle position (default is 0).
            id (int): Optional ID for the instance (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            """ if value is less or equal to 0 """
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            """ if value is less or equal to 0 """
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x if int > 0 """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            """ if value is less or equal to 0 """
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y if int > 0 """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            """ if value is less or equal to 0 """
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout rectangle instance with the character # """
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Update rectangle attributes with the provided arguments
        Args:
            *args: Variable number of arguments in the order
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            """ loop through the items """
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Override the __str__ method to return a custom str rep """
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle.

        Returns:
            dict: contains id, width, height, x, and y attributes.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
