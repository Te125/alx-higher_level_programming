#!/usr/bin/python3
""" square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of square position (default is 0).
            y (int): Y-coordinate of square position (default is 0).
            id (int): Optional ID for the instance (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Square attributes with the provided arguments

        Args:
            *args: List of positional arguments in the order (id, size, x, y).
            **kwargs: Dictionary of keyword arguments (attribute=value).
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            """ loop through the args """
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            """ loop through the kwargs item """
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override the __str__ method to return a custom str rep """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Return a dictionary representation of the Square.

        Returns:
            dict: A dictionary containing id, size, x, and y attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
