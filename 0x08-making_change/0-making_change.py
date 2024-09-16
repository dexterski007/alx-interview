#!/usr/bin/python3
""" make change function """


def makeChange(coins: list[int], total: int) -> int:
    """ make change function """
    if total <= 0:
        return 0
    coin_num = 0
    sorted_list = sorted(coins, reverse=True)
    wallet = {}
    for coin in sorted_list:
        if total == 0:
            break
        change = total // coin
        total -= change * coin
        wallet[coin] = change
        coin_num += change
    if total == 0:
        return coin_num
    else:
        return -1
