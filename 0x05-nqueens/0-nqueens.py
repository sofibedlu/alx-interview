#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at the given position (row, col)
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(board, row):
        if row == N:
            # Print the solution in the required format
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1

    board = [-1] * N
    backtrack(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

