def is_safe(board, x, y, n):
    for i in range(x):
        if board[i][y] == 1:
            return False

    i, j = x, y
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = x, y
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def n_queen(board, x, n):
    if x >= n:
        return True

    for y in range(n):
        if is_safe(board, x, y, n):
            board[x][y] = 1

            if n_queen(board, x + 1, n):
                return True

            board[x][y] = 0

    return False

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()


n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

if n_queen(board, 0, n):
    print_board(board)
else:
    print("Not possible")
