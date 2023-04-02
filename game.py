from mcst import *

def get_next_best_move(state: np.array, player: int) -> int:
    positions = possible_moves(state)
    best_pos = -1
    total = 0
    res = np.zeros((9,2))
    if len(positions) == 0:
        return best_pos
    for pos in positions:
        n, w = walkdown(next_state(np.copy(state), player, pos), player, get_next_player(player), 1, 0)
        res[pos] = [n, w]
        total += n
    vals = np.zeros(9)
    for i in range(9):
        if res[i][0] != 0:
            vals[i] = res[i][1] / res[i][0] + np.sqrt(2 * np.log(total) / res[i][0])
    best_pos = np.argmax(vals)
    return best_pos

# print(get_next_best_move(np.array([[1,0,-1],[1,-1,0],[0,1,-1]]), -1))