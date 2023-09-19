#!/usr/bin/python3
""" class module """


class Base:
    """Base class for managing id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class.

        Args:
            id (int): optional integer ID for the instance.
        """
        if id is not None:
            """ assign the public instance attrinute id if it is none """
            self.id = id
        else:
            """ otherwise increment nb_objects and assign new value """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
