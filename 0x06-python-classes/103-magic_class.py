#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, pipox=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__pipox = 0
        if type(pipox) is not int and type(pipox) is not float:
            raise TypeError("radius must be a number")
        self.__pipox = pipox

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__pipox ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__pipox)
