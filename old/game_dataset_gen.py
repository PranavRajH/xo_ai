import numpy as np
import csv

def is_place_available(arr: np.array, x: int,y: int):
    if (arr[x][y] != 0):
        return False
    return True

def next_turn(arr: np.array ,player: int):
    print(f"{player} Turn:")
    x = int(input("Row : "))
    y = int(input("Column : "))
    while (x<0 or x>2 or y<0 or y>2 or (not is_place_available(arr, x, y))):
        print("Give Proper Input")
        x = int(input("Row : "))
        y = int(input("Column : "))
    arr[x][y]=player

def winner(arr: np.array):
    for i in range(3):
        if ((arr[i][0] == arr[i][1] == arr[i][2]) and (arr[i][0] != 0)):
            return arr[i][0]
        if ((arr[0][i] == arr[1][i] == arr[2][i]) and (arr[0][i] != 0)):
            return arr[0][i]
    if ((arr[0][0] == arr[1][1] == arr[2][2]) and (arr[0][0] != 0)):
        return arr[0][0]
    if ((arr[0][2] == arr[1][1] == arr[2][0]) and (arr[0][2] != 0)):
        return arr[0][2]
    if (all([all([arr[i][j] != 0 for j in range(3)]) for i in range(3)])):
        return -1
    return None

def flip(arr: np.array, side: str = "horizontal"):
    if (side=="horizontal"):
        arr = np.array([arr[j][::-1] for j in range(3)], dtype="int8")
    elif (side=="vertical"):
        arr = np.array(arr[::-1], dtype="int8")
    elif (side=="diagonal"):
        arr = np.array([[arr[j][i] for j in range(3)] for i in range(3)], dtype="int8")
    elif (side=="anti-diagonal"):
        arr = np.array([[arr[2-j][i] for j in range(3)] for i in range(3)], dtype="int8")
    return arr

def gen_fips(arr):
    return [arr, flip(arr, "horizontal"), flip(arr, "vertical"), flip(arr, "diagonal"), flip(arr, "anti-diagonal")]

def write_game(x: list, y: list):
    writer = csv.writer(open("dataset4.csv", "a"))
    for a,b in zip(x, y):
        board = gen_fips(a)
        move = gen_fips(b)
        for a,b in zip(board, move):
            next = np.argmax(b.reshape((9,)) - a.reshape((9,)))
            print(b,a,next)
            
            writer.writerow(np.concatenate([a.reshape((9,)), [next]]))

while True:
    arr = np.zeros((3,3), dtype="int8")
    x = [arr.copy()]
    y = []
    while (not winner(arr)):
        "Player 1 Turn:"
        print(arr)
        next_turn(arr, 1)
        y.append(arr.copy())
        if (winner(arr)==1):
            write_game(x, y)
            break

        "Check for Draw"
        if (winner(arr)==-1):
            write_game(x, y)
            break
        
        "Player 2 Turn:"
        print(arr)
        next_turn(arr, 2)
        x.append(arr.copy())
        if (winner(arr)==2):
            write_game(y, x[1:])
            break
    
    if input("Play Again? (y/n) : ") == "n":
        break

print("Dataset Generated")