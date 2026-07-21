#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """Base class for geometry classes."""

    def area(self):
        """Raises an Exception, since area() is not implemented here."""
        raise Exception("area() is not implemented")
