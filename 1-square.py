#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Defines a square by its private instance attribute size."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: the size of the square
        """
        self.__size = size
