#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_ascending(self):
        """Tests a list in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        """Tests a list not in any particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_ordered_descending(self):
        """Tests a list in descending order."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Tests a list with a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Tests an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Tests calling with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Tests a list of negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_positive_negative(self):
        """Tests a list with both positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, -3, 8, 0]), 8)

    def test_all_same_values(self):
        """Tests a list where all values are identical."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_at_start(self):
        """Tests a list where the max value is the first element."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Tests a list where the max value is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_floats(self):
        """Tests a list containing floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_two_elements(self):
        """Tests a list with exactly two elements."""
        self.assertEqual(max_integer([3, 9]), 9)


if __name__ == "__main__":
    unittest.main()
