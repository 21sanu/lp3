
# N-Queens Problem using Backtracking
# First queen is fixed at row 1, column 1.

def is_safe(board, row, col, n):
    # Check the same column in previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All queens have been placed
    if row == n:
        return True

    # Try each column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


n = int(input("Enter the value of N: "))

if n <= 0:
    print("N must be a positive integer.")
else:
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Fix the first queen at the top-left corner
    board[0][0] = 1

    if solve_n_queens(board, 1, n):
        print("\nFinal N-Queens Matrix:")
        for row in board:
            print(*row)
    else:
        print("No solution exists with the first queen fixed at (1, 1).")
