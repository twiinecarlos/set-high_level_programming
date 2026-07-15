#!/usr/bin/python3
"""Module that defines a printable Rectangle class."""


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

    def area(self):
        """Returns the current area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the current perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle.

        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        for _ in range(self.__height):
            lines.append("#" * self.__width)
        return "\n".join(lines)
