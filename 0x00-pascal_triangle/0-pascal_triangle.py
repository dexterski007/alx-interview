#!/usr/bin/python3
"""
pascal triangle function
"""


def pascal_triangle(n):
    """ pascal triangle function """
    new_list = []
    for line in range(0, n):
        actual_row = [1] * (line + 1)
        for row in range(1, line):
            actual_row[row] = (new_list[line - 1][row - 1]
                               + new_list[line - 1][row])
        new_list.append(actual_row)
    return new_list
