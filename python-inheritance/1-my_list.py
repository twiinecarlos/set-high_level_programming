#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """List subclass that adds a sorted print method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
