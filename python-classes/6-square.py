#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Defines a square by its private size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square.

        Args:
            size: the size of the square (default 0)
            position: the position of the square (default (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value: the new position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError(
                "position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character, using position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
