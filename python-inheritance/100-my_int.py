#!/usr/bin/python3
"""Module that defines a MyInt class with inverted equality operators."""


class MyInt(int):
    """Integer subclass with == and != operators inverted."""

    def __eq__(self, value):
        """Returns True if self and value are not equal, otherwise False."""
        return int(self) != int(value)

    def __ne__(self, value):
        """Returns True if self and value are equal, otherwise False."""
        return int(self) == int(value)
