#!/usr/bin/python3
"""
define isWinner function
"""


def isWinner(x, nums):
    """
    Determine the winner of a game played for multiple rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list[int]): A list of integers representing the values of 'n'
                          for each round.

    Returns:
        str or None: The name of the player who won the most
                     rounds ('Maria' or 'Ben').
                     If there's no clear winner, None is returned.

    Note:
        The game is played by taking turns choosing prime numbers from the
        set of consecutive integers starting from 1 up to and including 'n'.
        The player who cannot make a move loses the game. Maria always goes
        first, and both players play optimally.

    Example:
        >> isWinner(5, [2, 5, 1, 4, 3])
        'Ben'
    """
    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    # Function to determine if a player can win for a given n
    def can_win(n):
        if n <= 1:
            return False
        return n % 2 == 0  # A player can win if n is even

    maria_wins = 0
    ben_wins = 0

    # Iterate through each round (each value of n)
    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner based on the number of rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
