#!/usr/bin/python3
"""Module that defines a function to safely add a new attribute."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: the object to add the attribute to
        name: the name of the new attribute
        value: the value of the new attribute

    Raises:
        TypeError: if the object can't have a new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
