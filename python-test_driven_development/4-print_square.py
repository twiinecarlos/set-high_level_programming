#!/usr/bin/python3
"""Module that defines a function to print a square of # characters."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: the size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
