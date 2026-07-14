#!/usr/bin/python3
"""
Zen of Python Refactoring Challenge
"""


# Verbose version: explicit loop and variables
# Zen principle: "Explicit is better than implicit"
def sum_even_verbose(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total


# Pythonic version: uses built-in sum() and generator expression
# Zen principles:
# - Simple is better than complex
# - Readability counts
def sum_even_pythonic(numbers):
    return sum(num for num in numbers if num % 2 == 0)


# Verbose version
# Zen principle: "Readability counts"
def longest_word_verbose(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Pythonic version: uses max() with key
# Zen principles:
# - Simple is better than complex
# - There should be one obvious way to do it
def longest_word_pythonic(words):
    return max(words, key=len)


# Verbose version
# Zen principle: "Explicit is better than implicit"
def filter_positive_verbose(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


# Pythonic version: list comprehension
# Zen principles:
# - Simple is better than complex
# - Beautiful is better than ugly
def filter_positive_pythonic(numbers):
    return [num for num in numbers if num > 0]
