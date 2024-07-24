#!/usr/bin/python3
""" pascal triangle module used to generate a pascal triangle
"""


def pascal_triangle(n):
    """creates a triangle of pascal based
    on the provided number
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for line in range(1, n):
        actual_row = [1]
        for row in range(1, line):
            item = triangle[line - 1][row - 1] + triangle[line - 1][row]
            actual_row.append(item)
        actual_row.append(1)
        triangle.append(actual_row)
    return triangle
