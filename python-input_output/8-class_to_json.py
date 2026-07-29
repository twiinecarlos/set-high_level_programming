#!/usr/bin/python3
"""Module that defines a function to convert an object to a dict
for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object for
    JSON serialization."""
    return obj.__dict__
