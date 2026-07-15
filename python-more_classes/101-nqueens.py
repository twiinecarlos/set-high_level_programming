#!/usr/bin/python3
"""N Queens puzzle solution."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at row and col."""
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    """Use backtracking to find all solutions."""
    if row == n:
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve(board, 0, n)
