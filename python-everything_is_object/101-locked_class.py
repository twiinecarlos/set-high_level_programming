#!/usr/bin/python3
"""Module that defines a LockedClass with restricted instance attributes."""


class LockedClass:
    """Class that only allows a first_name instance attribute."""

    __slots__ = ["first_name"]
