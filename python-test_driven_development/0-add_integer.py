#!/usr/bin/python3
"""Module that defines a function to add two integers.

This module contains a single function, add_integer, which adds
two numbers together after validating and casting them to integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Returns the sum of a and b, casting floats to int first."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
