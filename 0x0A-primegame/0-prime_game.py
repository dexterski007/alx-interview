#!/usr/bin/python3
""" prime game in python """


def primelist(num):
    """ function to create and return prime lists"""
    primes = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (primes[p]):
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, num + 1) if primes[p]]
    return prime_numbers


def isWinner(x, nums):
    """ function to select the winner """
    if not x or not nums:
        return None
    Maria = 0
    Ben = 0
    for i in range(x):
        primes = primelist(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
