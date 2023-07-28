#!/usr/bin/python3
"""
define validUTF8 function
"""


def validUTF8(data):
    """"
    determines if a given data set represents a valid UTF-8 encoding.
    """
    def is_valid_following_byte(byte):
        return 0b10000000 <= byte <= 0b10111111

    def get_byte_length(byte):
        if byte & 0b10000000 == 0:
            return 1
        elif byte & 0b11100000 == 0b11000000:
            return 2
        elif byte & 0b11110000 == 0b11100000:
            return 3
        elif byte & 0b11111000 == 0b11110000:
            return 4
        else:
            return 0  # Invalid byte

    index = 0
    while index < len(data):
        byte = data[index]
        length = get_byte_length(byte)

        if length == 0:
            return False  # Invalid byte encountered

        for i in range(1, length):
            index += 1
            if index >= len(data) or not is_valid_following_byte(data[index]):
                return False  # Invalid following byte

        index += 1

    return True
