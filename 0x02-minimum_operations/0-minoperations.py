#!/usr/bin/python3
""" module to determine minimum operations
"""


def minOperations(n):
    """ function to determine minimum operations needed
    to achieve the desired result!
    """
    if n <= 1:
        return 0
    operation = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operation += factor
            n //= factor
        factor += 1
    return operation
