import numpy as np

def new_board():
    return np.zeros((3,3))

def next_state(state: np.array, player: int, pos: int):
    row = pos // 3
    col = pos % 3
    state[row][col] = player
    
    return state

def next_player(player: int):
    return -player

def is_valid_move(state: np.array, pos: int):
    row = pos // 3
    col = pos % 3
    return state[row][col] == 0

def is_win(state: np.array, player: int, pos: int):
    row = pos // 3
    col = pos % 3
    state[row][col] = player
    
    return (np.sum(state[row, :]) == 3*player 
        or np.sum(state[:, col]) == 3*player
        or np.sum(np.diag(state)) == 3*player
        or np.sum(np.diag(np.flip(state))) == 3*player)

def is_draw(state: np.array):
    return (np.sum(np.reshape(state, -1) == 0) == 0)

if __name__ == '__main__':
    while True:
        board = new_board()
        print(board)
        player = 1
        pos = int(input(f'{player}:'))
        while not (is_win(board, player, pos) or is_draw(board)):
            board = next_state(board, player, pos)
            print(board)
            player = next_player(player)
            pos = int(input(f'{player}:'))
        else:
            if is_win(board, player, pos):
                print(f'{player} wins')
            else:
                print('Draw')
        if input(':') == 'q':
            break
