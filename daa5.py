def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row+1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter N: "))
board = [[0]*n for i in range(n)]

if n > 0:
    board[0][0] = 1

    if solve(board, 1, n):
        print("N Queens Matrix:")
        for row in board:
            print(*row)
    else:
        print("No solution exists")
else:
    print("Enter positive N")