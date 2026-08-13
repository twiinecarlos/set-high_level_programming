#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square.

        Args:
            size: the size of the square
            x: the horizontal offset (default 0)
            y: the vertical offset (default 0)
            id: the id of the instance (default None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates attributes via a list of ordered arguments, or a
        dictionary of key/value pairs.

        Args:
            *args: id, size, x, y (in that order)
            **kwargs: key/value pairs of attributes to update
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
