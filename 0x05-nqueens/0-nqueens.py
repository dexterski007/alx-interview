#!/usr/bin/python3
""" Nqueens task performance. """
import sys


def nqueens():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solver(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


def solver(N):
    def recurse(row, board):
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if safe(board, row, col):
                board[row] = col
                recurse(row + 1, board)
                board[row] = -1
    result = []
    board = [-1] * N
    recurse(0, board)
    return result


def safe(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
         board[i] + i == col + row:
            return False
    return True


if __name__ == "__main__":
    nqueens()
