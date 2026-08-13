#!/usr/bin/python3
"""Module that defines the Base class."""
import json


class Base:
    """Base class that manages the id attribute of all future classes
    and provides serialization/deserialization helpers."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id: the id of the new instance. If None, a new id is
                assigned based on the number of instances created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dicts.

        Args:
            list_dictionaries: a list of dictionaries

        Returns:
            "[]" if list_dictionaries is None or empty, otherwise the
            JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by a JSON string.

        Args:
            json_string: a string representing a list of dictionaries

        Returns:
            An empty list if json_string is None or empty, otherwise
            the Python list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary: key/value pairs of attributes to initialize
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from <ClassName>.json.

        Returns:
            An empty list if the file doesn't exist, otherwise a list
            of instances of cls built from the file's content.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of
        objects to a file named <ClassName>.json.

        Args:
            list_objs: a list of instances who inherit from Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))
