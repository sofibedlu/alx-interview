#!/usr/bin/python3

"""
define a function validUTF8
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid
    UTF-8 enconding
    the data set represented by a list of integers
    """

    for item in data:
        if not (item >= 0x00 and item <= 0xFF):
            return False

    return True
