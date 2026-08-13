#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import io
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_width_height_x_y(self):
        """Tests that all attributes are correctly assigned."""
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 9)
        self.assertEqual(r.id, 5)

    def test_default_x_y(self):
        """Tests the default values of x and y are 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        """Tests the area computation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_width_not_int(self):
        """Tests that a non-integer width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Tests that a non-integer height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_negative(self):
        """Tests that a negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_width_zero(self):
        """Tests that a width of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_negative(self):
        """Tests that a negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_not_int(self):
        """Tests that a non-integer x raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")

    def test_x_negative(self):
        """Tests that a negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_not_int(self):
        """Tests that a non-integer y raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "9")

    def test_y_negative(self):
        """Tests that a negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -9)

    def test_str(self):
        """Tests the __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_offset(self):
        """Tests display() with no x/y offset."""
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_offset(self):
        """Tests display() with x/y offsets."""
        r = Rectangle(2, 2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Tests update() with ordered positional arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_update_args_partial(self):
        """Tests update() with fewer positional arguments than
        attributes; the remaining attributes should be unchanged."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_update_kwargs(self):
        """Tests update() with keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(x=1, height=2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.height, 2)

    def test_to_dictionary(self):
        """Tests the to_dictionary representation."""
        r = Rectangle(10, 2, 1, 9, 8)
        self.assertEqual(
            r.to_dictionary(),
            {"id": 8, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_roundtrip(self):
        """Tests that a Rectangle rebuilt from to_dictionary() is
        equivalent to the original."""
        r1 = Rectangle(10, 2, 1, 9, 8)
        r2 = Rectangle(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_is_subclass(self):
        """Tests that Rectangle inherits from Base."""
        from models.base import Base
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Base)


if __name__ == "__main__":
    unittest.main()
