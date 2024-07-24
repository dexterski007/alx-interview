#!/usr/bin/python3
""" pascal triangle module used to generate a pascal triangle
"""


def pascal_triangle(n):
    """creates a triangle of pascal based
    on the provided number
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for line in range(n):
        actual_row = []
        for row in range(line + 1):
            if row == 0 or line == row:
                actual_row.append(1)
            elif row > 0 and line > 0:
                actual_row.append(triangle[line - 1][row - 1]
                                  + triangle[line - 1][row])
        triangle.append(actual_row)
    return triangle
