#!/usr/bin/python3
"""Module that defines a Student class with JSON conversion."""


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

    def to_json(self):
        """Retrieves a dictionary representation of the Student."""
        return self.__dict__
