from zen_golf import *
import inspect


def count_characters(code):
    return len(code.replace(" ", "").replace("\n", ""))


def avg_line_length(code):
    lines = [line for line in code.split("\n") if line.strip()]
    return sum(len(line) for line in lines) / len(lines)


functions = [
    sum_even_verbose,
    sum_even_pythonic,
    longest_word_verbose,
    longest_word_pythonic,
    filter_positive_verbose,
    filter_positive_pythonic
]


for func in functions:
    source = inspect.getsource(func)

    print(func.__name__)
    print("Characters:", count_characters(source))
    print("Average line length:", round(avg_line_length(source), 2))
    print("----------------")
