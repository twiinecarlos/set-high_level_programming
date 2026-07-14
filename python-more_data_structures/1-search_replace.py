#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list.

    Args:
        my_list: The original list.
        search: The element to replace.
        replace: The new element.

    Returns:
        A new list with replaced values.
    """
    return [replace if item == search else item for item in my_list]
