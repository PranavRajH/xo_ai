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
    print(vals)
    best_pos = np.argmax(vals)
    return best_pos

# print(get_next_best_move(np.array([[1,0,-1],[1,-1,0],[0,1,-1]]), -1))

if __name__ == '__main__':
    while True:
        board = new_board()
        print(board)
        player = 1
        pos = int(input(f'{player}:'))
        while not (is_win(board, player, pos) or is_draw(board)):
            board = next_state(board, player, pos)
            print(board)
            player = get_next_player(player)
            if player == 1:
                pos = int(input(f'{player}:'))
            else:
                pos = get_next_best_move(board, player)
                print(f'{player}: {pos}')
        else:
            if is_win(board, player, pos):
                print(f'{player} wins')
            else:
                print('Draw')
        if input(':') == 'q':
            break