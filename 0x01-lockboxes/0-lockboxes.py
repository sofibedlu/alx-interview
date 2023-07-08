#!/usr/bin/python3

"""
define a function canUnlockAll
"""


def canUnlockAll(boxes):
    """
    determine if all the boxes can be opened
    """
    openedBoxes = [False] * len(boxes)
    openedBoxes[0] = True
    stack = [0]

    while stack:
        currentBox = stack.pop()
        for key in boxes[currentBox]:
            if(key >= 0 and key < len(boxes) and openedBoxes[key] is False):
                openedBoxes[key] = True
                stack.append(key)

    return all(openedBoxes)
