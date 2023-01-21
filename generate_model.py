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

for order in permutations([0,1,2,3,4,5,6,7,8]):
    arr = np.zeros((9,))
    xtrain = []
    ytrain = [arr.copy()]
    for i,pos in enumerate(order):
        if i%2==0:
            arr[pos] = 1
            xtrain.append(arr.copy())
        else:
            arr[pos] = 2
            ytrain.append(arr.copy())
        win = winner(arr.reshape((3,3)))
        if win != None:
            if win == 1:
                model = train_model(model, ytrain, xtrain)
            elif win == 2:
                model = train_model(model, xtrain, ytrain[1:])
            else:
                model = train_model(model, ytrain, xtrain)
            break
    count += 1
    print("%.3f"%((count/362880)*100), end='\r')

print("Training complete")
save_model(model)