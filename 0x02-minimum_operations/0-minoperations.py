#!/usr/bin/python3

"""
define minOperations function
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """

    if n <= 1 or not isinstance(n, int):
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
