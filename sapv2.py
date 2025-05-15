import random

def create_board(rows, cols, mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    placed_mines = 0
    while placed_mines < mines:
        row = random.randint(0, rows-1)
        col = random.randint(0, cols-1)
        if board[row][col] != 'X':
            board[row][col] = 'X'
            placed_mines += 1
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def count_adjacent_mines(board, row, col):
    count = 0
    rows = len(board)
    cols = len(board[0])
    for i in range(max(0, row-1), min(row+2, rows)):
        for j in range(max(0, col-1), min(col+2, cols)):
            if board[i][j] == 'X':
                count += 1
    return count

def reveal_square(board, row, col):
    if board[row][col] != ' ':
        return
    mines = count_adjacent_mines(board, row, col)
    board[row][col] = str(mines)
    if mines == 0:
        rows = len(board)
        cols = len(board[0])
        for i in range(max(0, row-1), min(row+2, rows)):
            for j in range(max(0, col-1), min(col+2, cols)):
                if board[i][j] == ' ':
                    reveal_square(board, i, j)

def play_game(rows, cols, mines):
    board = create_board(rows, cols, mines)
    print_board(board)
    while True:
        row = int(input("Введите строку: "))
        col = int(input("Введите столбец: "))
        if board[row][col] == 'X':
            print("Game Over!")
            print("Проигрыш!")
            break
        else:
            reveal_square(board, row, col)
            print_board(board)
            if all(' ' not in row for row in board):
                print("Победа!")
                break

play_game(10, 10, 10)
