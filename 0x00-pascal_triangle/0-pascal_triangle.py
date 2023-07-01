#!/usr/bin/python3


"""
pascal-traingle
"""


def pascal_triangle(n):
    """
    Args:
        n (int): traingle of n
    Returns:
        -list of lists integers
        -empty list if n <= 0
    """

    tri = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                value = tri[i - 1][j - 1] + tri[i - 1][j]
                row.append(value)
        tri.append(row)
    return tri
