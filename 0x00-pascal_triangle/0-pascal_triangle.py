#!/usr/bin/python3
''' pascal triangle function '''


def pascal_triangle(n):
    ''' pascal triangle function '''
    new_list = []
    if n <= 0:
        return new_list
    for line in range(n):
        actual_row = []
        for row in range(line + 1):
            if row == 0 or line == row:
                actual_row.append(1)
            elif row > 0 and line > 0:
                actual_row.append(new_list[line - 1][row - 1]
                               + new_list[line - 1][row])
        new_list.append(actual_row)
    return new_list
