#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, using Rectangle's validation and area logic."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: the size of the square
        """
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return super().area()
