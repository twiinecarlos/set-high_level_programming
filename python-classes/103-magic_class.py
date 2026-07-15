#!/usr/bin/python3
"""Module that defines MagicClass, matching a given bytecode."""
import math


class MagicClass:
    """Defines a circle with a radius, matching the given bytecode."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass.

        Args:
            radius: the radius of the circle (default 0)

        Raises:
            TypeError: if radius is not a number
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle."""
        return 2 * math.pi * self.__radius
