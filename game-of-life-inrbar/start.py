import numpy as np

def create_board_predef(name):
    # global board
    board = np.empty((0,0))

    with open(f'sample_patterns/{name}.txt', 'r') as file:
        src = file.read()

    new_line_count = 0
    for i in src:
        if i == '\n':
            new_line_count += 1
            continue
        board = np.append(board, i)

    
    y_len = new_line_count + 1
    x_len = int(board.size / y_len)

    for k in range(board.size):
        if board[k] == 'X':
            board[k] = 1
        else:
            board[k] = 0

    board = board.reshape(y_len,x_len)
    board = board.astype(int)
    return board

def create_board_random(size):
    int_size = [int(x) for x in size]
    y_len, x_len = int_size
    board = np.random.choice([0,1], x_len*y_len).reshape(y_len, x_len)
    return board