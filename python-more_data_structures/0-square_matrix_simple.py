#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix: A 2D list of integers.

    Returns:
        A new matrix with each value squared.
    """
    return [[number ** 2 for number in row] for row in matrix]
