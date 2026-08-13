#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_public(self):
        """Tests that the id given is used correctly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        """Tests that an id is auto-assigned when None is passed."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_default(self):
        """Tests that an id is auto-assigned with no argument."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_none(self):
        """Tests to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Tests to_json_string with an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Tests to_json_string with a real list of dictionaries."""
        list_input = [{"id": 1}, {"id": 2}]
        json_output = Base.to_json_string(list_input)
        self.assertEqual(Base.from_json_string(json_output), list_input)

    def test_from_json_string_none(self):
        """Tests from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Tests from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_save_to_file_none(self):
        """Tests save_to_file with None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_list(self):
        """Tests save_to_file with a real list of instances."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"id": {}'.format(r1.id), content)
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Tests load_from_file when the file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_round_trip_rectangle(self):
        """Tests that saving and loading Rectangles preserves data."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())
        os.remove("Rectangle.json")

    def test_save_and_load_round_trip_square(self):
        """Tests that saving and loading Squares preserves data."""
        s1 = Square(2)
        s2 = Square(3, 5, 5)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), s2.to_dictionary())
        os.remove("Square.json")

    def test_create_rectangle(self):
        """Tests that create() builds a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Tests that create() builds a Square from a dictionary."""
        s1 = Square(3, 1, 2, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()
