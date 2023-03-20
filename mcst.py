import numpy as np

from TicTacToe import *


def possible_moves(state: np.array) -> list:
    return [i for i in range(9) if state.reshape(-1)[i] == 0]


def walkdown(state: np.array, player: int, next_player: int, n: int, w: int) -> int:
    positions = possible_moves(state)
    print(state, player, next_player, n, w, positions)
    if len(positions) == 1:
        if is_win(state, player, positions[0]):
            return n + 1, w + 1
        else:
            return n + 1, w
    else:
        num = 0
        wins = 0
        print("in loop")
        for pos in positions:
            if is_win(state, next_player, pos):
                num += 1
                if next_player == player:
                    wins += 1
                continue
            new_state = next_state(np.copy(state), next_player, pos)
            new_n, new_w = walkdown(np.copy(new_state), player, get_next_player(next_player), n, w)
            num += new_n
            wins += new_w
            print(new_state, player, next_player, new_n, new_w, num, wins)
        print("out loop")
        return num, wins


"""
    print(walkdown(np.zeros((3,3)), -1, -1, 1, 0))
    To find the tree of all possible games of TicTacToe
"""
