#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height."""


class Rectangle:
    """Defines a rectangle by its private width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width: the width of the rectangle (default 0)
            height: the height of the rectangle (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: the new width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: the new height

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
