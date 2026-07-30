#!/usr/bin/python3
"""Module that defines a function to multiply two matrices using NumPy."""
import numpy as np


def validate_matrix(matrix, name):
    """Validates that matrix is a non-empty rectangular list of
    lists of integers/floats, raising errors named after `name`."""
    if type(matrix) is not list:
        raise TypeError("{} must be a list".format(name))

    if not all(type(row) is list for row in matrix):
        raise TypeError("{} must be a list of lists".format(name))

    if matrix == [] or matrix == [[]]:
        raise ValueError("{} can't be empty".format(name))

    for row in matrix:
        if not all(type(x) is int or type(x) is float for x in row):
            raise TypeError(
                "{} should contain only integers or floats".format(name))

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(
            "each row of {} must be of the same size".format(name))


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
