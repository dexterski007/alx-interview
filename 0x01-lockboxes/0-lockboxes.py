#!/usr/bin/python3
""" module to determine if boxes can be unlocked
"""


def canUnlockAll(boxes):
    """ unlock tester function """
    n = len(boxes)
    unlocked_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked_boxes and new_key < n:
            unlocked_boxes.add(new_key)
            keys.update(boxes[new_key])
    print (unlocked_boxes)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
