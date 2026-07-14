#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number and returns its value."""
    last_digit = number % 10
    if number < 0 and last_digit != 0:
        last_digit -= 10
    if last_digit < 0:
        last_digit *= -1
    print("{:d}".format(last_digit), end="")
    return last_digit
