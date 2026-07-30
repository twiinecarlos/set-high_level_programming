#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix.

This module contains a single function, matrix_divided, which
validates a matrix and a divisor, then returns a new matrix with
every element divided and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Returns a new matrix; the original matrix is left unchanged."""
    if (type(matrix) is not list or len(matrix) == 0 or
            not all(type(row) is list for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(type(x) is int or type(x) is float for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
