#!/usr/bin/python3
""" Class square module """


class Square:
    """ This class defines a square by its size.
    """

    def __init__(self, size=0):
        """ Initializes a new Square instance.

        Args:
            size (number): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """ Getter for the size of the square.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square.

        Args:
            value (number): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """ Define behavior for the == operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Define behavior for the != operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Define behavior for the > operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Define behavior for the >= operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Define behavior for the < operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """ Define behavior for the <= operator.

        Args:
            other (Square): Another Square object.

        Returns:
            bool: True if area is less or equal, False otherwise.
        """
        return self.area() <= other.area()
