#!/usr/bin/python3
""" 2d matrix rotation """


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix module """
    length = len(matrix)
    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(length):
        matrix[i].reverse()
