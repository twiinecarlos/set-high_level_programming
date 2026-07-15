#!/usr/bin/python3
"""Module that defines a Square class with comparison operators."""


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
            TypeError: if value is not a number
            ValueError: if value is less than 0
        """
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Checks if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if this square's area is greater than other's."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if this square's area is greater than or equal."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if this square's area is less than other's."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if this square's area is less than or equal."""
        return self.area() <= other.area()
