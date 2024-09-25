#!/usr/bin/python3
"""
function to calculate island perimeters
"""


def island_perimeter(grid):
    """ island calculator function """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                count += 4
                if grid[i - 1][j] == 1:
                    count -= 1
                if grid[i + 1][j] == 1:
                    count -= 1
                if grid[i][j - 1] == 1:
                    count -= 1
                if grid[i][j + 1] == 1:
                    count -= 1
    return count
