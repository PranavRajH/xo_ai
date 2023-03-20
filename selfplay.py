import numpy as np

from keras import layers, Sequential
from TicTacToe import *

model = Sequential(
    [
        layers.Dense(18, input_shape=(9,), activation="tanh"),
        layers.Dense(36),
        layers.Dense(72),
        layers.Dense(36),
        layers.Dense(18),
        layers.Dense(9, activation="tanh"),
    ]
)

model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])

try:
    while True:
        board = new_board()
        print(board)
        player = 1
        pos = np.argmax((player * model.predict(board.reshape(1, 9))))
        while not (is_win(board, player, pos) or is_draw(board)):
            board = next_state(board, player, pos)
            print(board)
            player = get_next_player(player)
            pred = np.array(list(model.predict(board.reshape(1, 9), verbose=0)))
            pos = np.argmax(player * pred)
            while not is_valid_move(board, pos):
                pred[0][pos] = (-1 * player)
                pos = np.argmax(player * pred)
        else:
            if is_win(board, player, pos):
                print(board)
                print(f'{player} wins')
            else:
                print('Draw')
        if input(':') == 'q':
            break
except KeyboardInterrupt:
    model.save('model.h5')