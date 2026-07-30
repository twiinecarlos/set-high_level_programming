#!/usr/bin/python3
"""Module that defines a function to print text with indentation
after certain punctuation characters."""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and : character.

    Args:
        text: the text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    current = ""
    for c in text:
        current += c
        if c in ".?:":
            print(current.strip())
            print()
            current = ""
    print(current.strip(), end="")
