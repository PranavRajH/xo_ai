import numpy as np

from TicTacToe import *

class Node:
    def __init__(self, state: np.array, player: int, parent = None, children: list = [], n: int = 1, w: int = 0, val: int = 0):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = children
        self.n = n
        self.w = w
        self.val = val

    def __str__(self):
        return f'state: \n{self.state}\nplayer: {self.player}\nn: {self.n}\nw: {self.w}\nval: {self.val}'

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
    
def mcst_gen(root: Node, player: int, next_player: int) -> Node:
    positions = possible_moves(root.state)
    if len(positions) == 1:
        if is_win(root.state, player, positions[0]):
            root.parent.children.append(Node(np.copy(root.state), player, root, n=1, w=1, val=1))
        else:
            root.parent.children.append(Node(np.copy(root.state), player, root, n=1, w=0, val=0))
    else:
        for pos in positions:
            if is_win(root.state, next_player, pos):
                if next_player == player:
                    root.children.append(Node(next_state(np.copy(root.state), next_player, pos), player, root, n=1, w=1, val=1))
                else:
                    root.children.append(Node(next_state(np.copy(root.state), next_player, pos), player, root, n=1, w=0, val=0))
                continue
            new_state = next_state(np.copy(root.state), next_player, pos)
            child = Node(new_state, player, root)
            child = mcst_gen(child, player, get_next_player(next_player))
            root.children.append(child)
    root.n += sum([child.n for child in root.children])
    root.w += sum([child.w for child in root.children])
    if root.parent:
        total = sum([child.n for child in root.parent.children])
    else:
        total = 1
    root.val = root.w / root.n + 0.5 * np.sqrt(2 * np.log(total) / root.n)
    return root

# print(walkdown(np.array([[1,0,-1],[1,-1,0],[0,1,-1]]), -1, -1, 1, 0, 1))
# print(mcst_gen(Node(np.array([[1,0,-1],[1,-1,0],[0,1,-1]]), -1), -1, -1))

"""
    print(walkdown(np.zeros((3,3)), -1, -1, 1, 0))
    To find the tree of all possible games of TicTacToe
"""
