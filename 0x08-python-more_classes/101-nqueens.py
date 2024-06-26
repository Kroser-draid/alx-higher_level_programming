#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N\n")
    sys.exit(1)
else:
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4\n")
            sys.exit(1)
    except ValueError:
        print("N must be a number\n")
        sys.exit(1)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    def solve(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * N
    solve(0)
    return solutions


solutions = solve_nqueens(N)
for solution in solutions:
    formatted_solution = []
    for row, col in enumerate(solution):
        formatted_solution.append([row, col])
    print(formatted_solution)
