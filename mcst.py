import numpy as np

from TicTacToe import *


def possible_moves(state: np.array) -> list:
    return [i for i in range(9) if state.reshape(-1)[i] == 0]


def walkdown(state: np.array, player: int, next_player: int, n: int, w: int, verbose: int = 0) -> int:
    print("walkdown")
    positions = possible_moves(state)
    if verbose:
        print(f'state: \n{state}\nplayer: {player}\nnext_player: {next_player}\nn: {n}\nw: {w}\npositions: {positions}')
    if len(positions) == 1:
        if is_win(state, player, positions[0]):
            if verbose:
                print("win")
            return n + 1, w + 1
        else:
            if verbose:
                print("draw")
            return n + 1, w
    else:
        num = 0
        wins = 0
        print("in loop")
        for pos in positions:
            num += 1
            if is_win(state, next_player, pos):
                if next_player == player:
                    if verbose:
                        print("win")
                    wins += 1
                continue
            new_state = next_state(np.copy(state), next_player, pos)
            new_n, new_w = walkdown(np.copy(new_state), player, get_next_player(next_player), n, w)
            num += new_n
            wins += new_w
            print(f'state: \n{new_state}\nplayer: {player}\nnext_player: {get_next_player(next_player)}\nn: {new_n}\nw: {new_w}\ncumulative n: {num}\ncumulative w: {wins}')
        print("out loop")
        return num, wins

"""
    print(walkdown(np.zeros((3,3)), -1, -1, 1, 0))
    To find the tree of all possible games of TicTacToe
"""
