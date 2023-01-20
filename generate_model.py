import numpy as np
from itertools import permutations

from model import *

def winner(arr):
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
            return 'D'
        return None

model = create_model()
print(model.summary())
count = num = 0

for i in range(9):
    combs = permutations(([0 for j in range(i)] + [1 for j in range((9-i)//2+1-i%2)] + [2 for j in range(9-i-(9-i)//2)]), 9)
    for comb in combs:
        arr = np.array(comb)
        if (winner(arr.reshape((3,3))) == 1):
            for j in arr:
                if arr[j]==1:
                    arr[j] = 0
                    hot_code = np.zeros((9,))
                    hot_code[j] = 1
                    model.fit(arr.reshape(1,3,3), hot_code.reshape(1,9), epochs=50, verbose=0)
        elif (winner(arr.reshape((3,3))) == 2):
            for j in arr:
                if arr[j]==2:
                    arr[j] = 0
                    hot_code = np.zeros((9,))
                    hot_code[j] = 1
                    model.fit(arr.reshape(1,3,3), hot_code.reshape(1,9), epochs=50, verbose=0)
        elif (winner(arr.reshape((3,3))) == 'D'):
            for j in arr:
                if arr[j]!=0:
                    arr[j] = 0
                    hot_code = np.zeros((9,))
                    hot_code[j] = 1
                    model.fit(arr.reshape(1,3,3), hot_code.reshape(1,9), epochs=50, verbose=0)
        else:
            count += 1
        num += 1
        print(num)

print(count)
save_model(model)