#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_size_x_y(self):
        """Tests that size, x, y, and id are correctly assigned."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 12)

    def test_width_equals_height(self):
        """Tests that width and height are both set to size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Tests the default values of x and y are 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_area(self):
        """Tests the area computation."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_size_not_int(self):
        """Tests that a non-integer size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_negative(self):
        """Tests that a negative size raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_size_zero(self):
        """Tests that a size of 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_setter(self):
        """Tests that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_str(self):
        """Tests the __str__ representation."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(str(s), "[Square] (12) 1/2 - 5")

    def test_update_args(self):
        """Tests update() with ordered positional arguments."""
        s = Square(10, 10, 10, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual(
            s.to_dictionary(), {"id": 1, "size": 2, "x": 3, "y": 4})

    def test_update_kwargs(self):
        """Tests update() with keyword arguments."""
        s = Square(10, 10, 10, 1)
        s.update(size=2, x=1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 1)

    def test_to_dictionary(self):
        """Tests the to_dictionary representation."""
        s = Square(5, 1, 2, 12)
        self.assertEqual(
            s.to_dictionary(), {"id": 12, "size": 5, "x": 1, "y": 2})

    def test_to_dictionary_no_width_height_keys(self):
        """Tests that to_dictionary uses size, not width/height."""
        s = Square(5)
        d = s.to_dictionary()
        self.assertNotIn("width", d)
        self.assertNotIn("height", d)
        self.assertIn("size", d)

    def test_is_subclass_of_rectangle(self):
        """Tests that Square inherits from Rectangle."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)


if __name__ == "__main__":
    unittest.main()
