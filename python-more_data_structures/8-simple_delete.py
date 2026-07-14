#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary. If the key doesn't exist,
    the dictionary won't change."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
