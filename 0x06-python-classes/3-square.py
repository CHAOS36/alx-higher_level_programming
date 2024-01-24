#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, sex=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(sex, int):
            raise TypeError("size must be an integer")
        elif sex < 0:
            raise ValueError("size must be >= 0")
        self.__sex = sex

    def area(self):
        """Return the current area of the square."""
        return (self.__sex * self.__sex)
