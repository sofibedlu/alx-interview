#!/usr/bin/python3
"""
define makechange
"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list[int]): A list of coin values available for use.
        total (int): The target amount to be achieved.

    Returns:
        int: The fewest number of coins needed to reach the total.
             If the total is 0 or less, returns 0.
             If the total cannot be met by any combination of coins,returns -1
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    # needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the minimum number of coins needed for each total
    # value from 1 to 'total'
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value at 'total' is still 'inf', it means the total cannot be met
    # by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
