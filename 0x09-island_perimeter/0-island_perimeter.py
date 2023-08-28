#!/usr/bin/python3
"""
island_perimeter_module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    grid (list of list of int): A rectangular grid representing the island.

    Returns:
    int: The perimeter of the island.

    Constraints:
    - Each cell is square with a side length of 1.
    - Cells are connected horizontally/vertically (not diagonally).
    - The grid is completely surrounded by water.
    - There is only one island (or nothing).
    - The island doesn't have "lakes" (water inside that isn't connected
    to the water surrounding the island).
    """

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Count all sides initially

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
