#!/usr/bin/python3
"""Module that defines a function to save an object as JSON to a file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
