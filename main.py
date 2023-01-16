import itertools as it
import random
import numpy as np

from tensorflow.keras import *

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

    def winner(self):
        for i in range(3):
            if ((self.arr[i][0] == self.arr[i][1] == self.arr[i][2]) and (self.arr[i][0] != ' ')):
                return self.arr[i][0]
            if ((self.arr[0][i] == self.arr[1][i] == self.arr[2][i]) and (self.arr[0][i] != ' ')):
                return self.arr[i][0]
        if ((self.arr[0][0] == self.arr[1][1] == self.arr[2][2]) and (self.arr[0][0] != ' ')):
            return self.arr[0][0]
        if ((self.arr[0][2] == self.arr[1][1] == self.arr[2][0]) and (self.arr[0][2] != ' ')):
            return self.arr[0][2]
        return None

if __name__=="__main__":
    board = Board()
    while (board.winner() == None):
        board.display()
        print("X turn")
        board.next_turn('X')
        if (board.winner() == 'X'):
            board.display()
            print("X wins")
            break
        board.display()
        print("O turn")
        board.next_turn('O')
        if (board.winner() == 'O'):
            board.display()
            print("Y wins")
            break
    
