#!/usr/bin/python3
"""Module that defines a function to multiply two matrices."""


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


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Returns a new matrix representing the product of m_a and m_b."""
    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
