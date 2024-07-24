#!/usr/bin/python3
""" pascal triangle module used to generate a pascal triangle
"""


def recursive_pascal(line, row):
    """recursive function for the calculation"""
    if row == 0 or line == row:
        return 1
    return (recursive_pascal(line - 1, row - 1)
            + recursive_pascal(line - 1, row))


def pascal_triangle(n):
    """creates a triangle of pascal based
    on the provided number
    """
    if n <= 0:
        return []
    triangle = []
    for line in range(n):
        sublist = []
        for row in range(line + 1):
            sublist.append(recursive_pascal(line, row))
        triangle.append(sublist)
    return triangle
