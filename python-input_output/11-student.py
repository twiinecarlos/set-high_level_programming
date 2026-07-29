#!/usr/bin/python3
"""Module that defines a Student class with JSON reload capability."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name: the student's first name
            last_name: the student's last name
            age: the student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student.

        Args:
            attrs: optional list of attribute names to filter by
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json: a dictionary of attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)

