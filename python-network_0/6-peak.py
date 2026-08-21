#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Return a peak from a list of unsorted integers."""
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        middle = (left + right) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            left = middle + 1
        else:
            right = middle

    return list_of_integers[left]
