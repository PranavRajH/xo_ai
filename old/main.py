import itertools as it
import random
import numpy as np
import keras

from model import *

class Board():
    def __init__(self):
        self.arr = [[' ' for i in range(3)] for j in range(3)]

    def display(self):
        print(f" {self.arr[0][0]} | {self.arr[0][1]} | {self.arr[0][2]} ")
        print("---+---+---")
        print(f" {self.arr[1][0]} | {self.arr[1][1]} | {self.arr[1][2]} ")
        print("---+---+---")
        print(f" {self.arr[2][0]} | {self.arr[2][1]} | {self.arr[2][2]} ")

    def is_place_available(self,x: int,y: int):
        if (self.arr[x][y] != ' '):
            return False
        return True

    def next_turn(self,player: str):
        x = int(input("Row : "))
        y = int(input("Column : "))
        while (x<0 or x>2 or y<0 or y>2 or (not self.is_place_available(x,y))):
            print("Give Proper Input")
            x = int(input("Row : "))
            y = int(input("Column : "))
        self.arr[x][y]=player

    def next_turn_ai(self,player: str, model: Sequential):
        count = 1
        predictions = model.predict(convert(self.arr).reshape(1,9), verbose=0)
        choice = np.argmax(predictions[0])
        x = choice//3
        y = choice%3
        while (x<0 or x>2 or y<0 or y>2 or (not self.is_place_available(x,y))):
            print(f"Trying : {count}")
            count += 1
            predictions[0][choice] = 0
            choice = np.argmax(predictions[0])
            x = choice//3
            y = choice%3
        self.arr[x][y] = player


    def winner(self):
        for i in range(3):
            if ((self.arr[i][0] == self.arr[i][1] == self.arr[i][2]) and (self.arr[i][0] != ' ')):
                return self.arr[i][0]
            if ((self.arr[0][i] == self.arr[1][i] == self.arr[2][i]) and (self.arr[0][i] != ' ')):
                return self.arr[0][i]
        if ((self.arr[0][0] == self.arr[1][1] == self.arr[2][2]) and (self.arr[0][0] != ' ')):
            return self.arr[0][0]
        if ((self.arr[0][2] == self.arr[1][1] == self.arr[2][0]) and (self.arr[0][2] != ' ')):
            return self.arr[0][2]
        if (all([all([self.arr[i][j] != ' ' for j in range(3)]) for i in range(3)])):
            return 'D'
        return None
    
    def clear(self):
        self.arr = [[' ' for i in range(3)] for j in range(3)]

def convert(array):
    arr = np.zeros((3,3), dtype="int8")
    for i in range(3):
        for j in range(3):
            if (array[i][j] == ' '):
                arr[i][j] = 0
            elif (array[i][j] == 'X'):
                arr[i][j] = 1
            else:
                arr[i][j] = 2
    return arr

def flip(arr, side: str = "horizontal"):
    if (side=="horizontal"):
        arr = [arr[j][::-1] for j in range(3)]
    elif (side=="vertical"):
        arr = arr[::-1]
    elif (side=="diagonal"):
        arr = [[arr[j][i] for j in range(3)] for i in range(3)]
    elif (side=="anti-diagonal"):
        arr = [[arr[2-j][i] for j in range(3)] for i in range(3)]
    return arr

def train_model(model, x, y):
    for x,y in zip(x_train, y_train):
        y = np.array([1 if(i!=0) else 0 for i in (y.reshape((9,)) - x.reshape((9,)))])
        model.fit(x.reshape(1,9), y.reshape(1,9), epochs=50, verbose=0)
    return model

if __name__=="__main__":
    model = keras.models.load_model("xo.h5")
    print(model.summary())
    board = Board()
    while True:
        board.clear()
        me = []
        comp = []
        while (board.winner() == None):
            board.display()
            print("X turn")
            comp.append(convert(board.arr))
            board.next_turn('X')
            if (board.winner() == 'X'):
                board.display()
                print("X wins")
                x_train = comp
                y_train = me+[board.convert()]
                model = train_model(model, x_train, y_train)
                model = train_model(model, [convert(flip(x)) for x in x_train], [convert(flip(y)) for y in y_train])
                model = train_model(model, [convert(flip(x, "vertical")) for x in x_train], [convert(flip(y, "vertical")) for y in y_train])
                model = train_model(model, [convert(flip(x, "diagonal")) for x in x_train], [convert(flip(y, "diagonal")) for y in y_train])
                model = train_model(model, [convert(flip(x, "anti-diagonal")) for x in x_train], [convert(flip(y, "anti-diagonal")) for y in y_train])
                break

            if (board.winner() == 'D'):
                board.display()
                print("Draw")
                x_train = comp
                y_train = me
                model = train_model(model, x_train, y_train)
                model = train_model(model, [convert(flip(x)) for x in x_train], [convert(flip(y)) for y in y_train])
                model = train_model(model, [convert(flip(x, "vertical")) for x in x_train], [convert(flip(y, "vertical")) for y in y_train])
                model = train_model(model, [convert(flip(x, "diagonal")) for x in x_train], [convert(flip(y, "diagonal")) for y in y_train])
                model = train_model(model, [convert(flip(x, "anti-diagonal")) for x in x_train], [convert(flip(y, "anti-diagonal")) for y in y_train])
                break

            board.display()
            print("O turn")
            me.append(convert(board.arr))
            board.next_turn('O')
            if (board.winner() == 'O'):
                board.display()
                print("O wins")
                x_train = me
                y_train = comp[1:]
                model = train_model(model, x_train, y_train)
                model = train_model(model, [convert(flip(x)) for x in x_train], [convert(flip(y)) for y in y_train])
                model = train_model(model, [convert(flip(x, "vertical")) for x in x_train], [convert(flip(y, "vertical")) for y in y_train])
                model = train_model(model, [convert(flip(x, "diagonal")) for x in x_train], [convert(flip(y, "diagonal")) for y in y_train])
                model = train_model(model, [convert(flip(x, "anti-diagonal")) for x in x_train], [convert(flip(y, "anti-diagonal")) for y in y_train])
        
        ch = input("Do you want to play again? (y/n) : ")
        if (ch == 'n'):
            model.save("xo.h5")
            break
    
