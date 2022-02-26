#zad z zestawu 5

import random


def chessboard(board):
    n = len(board)
    helper_board = [[0 for _ in range(n)] for _ in range(n)]
    helper_board[0][0] = board[0][0]

    for y in range(n):
        for x in range(n):
            if x == 0:
                helper_board[y][x] = helper_board[y-1][x] + board[y][x]
            elif y == 0:
                helper_board[y][x] = helper_board[y][x-1] + board[y][x]

            else:
                helper_board[y][x] = min(helper_board[y-1][x], helper_board[y][x-1]) + board[y][x]

    print(helper_board[n-1][n-1])

chess = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
chessboard(chess)
for lane in chess:
    print(lane)