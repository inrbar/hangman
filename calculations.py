import numpy as np

def neighbour_check(board, x, y, len_y, len_x):
    alive_num = 0
    for i in range(-1,2):
        row = y + i
        if row >=0 and row <= len_x - 1:
            for j in range(-1,2):
                collumn = x + j
                if collumn >= 0 and collumn <= len_y - 1:
                    if collumn == x and row == y:
                        continue
                    elif board[collumn, row] == 1:
                        alive_num += 1
    return alive_num

def logic(board):
    len_y, len_x = board.shape
    # creating new array to keep track of every cells number of neighbours
    alive_array = np.empty((len_y, len_x), int)
    new_board = np.empty((len_y, len_x), int)

    # checking num of neighbours and assigning it to its respective cell
    for i in range(len_y):
        for k in range(len_x):
            alive_num = neighbour_check(board, i, k, len_y, len_x)
            alive_array[i,k] = alive_num
    
    # basic game logic
    for i in range(len_y):
        for k in range(len_x):
            if (alive_array[i,k] < 2 or alive_array[i,k] > 3):
                new_board[i,k] = 0
            elif alive_array[i,k] == 3:
                new_board[i,k] = 1
            elif alive_array[i,k] == 2 or alive_array[i,k] == 3:
                new_board[i,k] = board[i,k]
    return new_board