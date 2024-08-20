#!/usr/bin/python3
""" module validate utf8
"""


def validUTF8(data):
    """ function to validate utf 8"""
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte & 0b10000000 == 0:
                continue
            if byte & 0b11100000 == 0b11000000:
                num_bytes += 1
            if byte & 0b11110000 == 0b11100000:
                num_bytes += 2
            if byte & 0b11111000 == 0b11110000:
                num_bytes += 3
            else:
                return False

        if num_bytes > 0:
            if not byte & 0b11000000 == 0b10000000:
                return False
            num_bytes -= 1
    if num_bytes == 0:
        return True
    return False
