#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Defines a square by its private instance attribute size."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size: the size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value: the new size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size
