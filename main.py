import itertools as it
import random
import numpy as np

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
        predictions = model.predict(self.convert().reshape(1,3,3), verbose=0)
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
    
    def convert(self):
        arr = np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                if (self.arr[i][j] == ' '):
                    arr[i][j] = 0
                elif (self.arr[i][j] == 'X'):
                    arr[i][j] = 1
                else:
                    arr[i][j] = 2
        return arr
    
    def clear(self):
        self.arr = [[' ' for i in range(3)] for j in range(3)]

if __name__=="__main__":
    model = create_model()
    print(model.summary())
    board = Board()
    while True:
        board.clear()
        me = []
        comp = []
        while (board.winner() == None):
            board.display()
            print("X turn")
            comp.append(board.convert())
            board.next_turn('X')
            if (board.winner() == 'X'):
                board.display()
                print("X wins")
                model = train_model(model, comp, me+[board.convert()])
                break
            board.display()
            print("O turn")
            me.append(board.convert())
            board.next_turn_ai('O', model)
            if (board.winner() == 'O'):
                board.display()
                print("O wins")
                model = train_model(model, me, comp[1:])
                break
        else:
            board.display()
            print("Draw")
            model = train_model(model, comp, me)
        
        ch = input("Do you want to play again? (y/n) : ")
        if (ch == 'n'):
            save_model(model)
            break
    
