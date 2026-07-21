#!/usr/bin/python3
"""Module that defines an inheritance-aware class-matching function."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass."""
    return isinstance(obj, a_class)
