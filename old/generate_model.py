import numpy as np
from pandas import read_csv
from model import *

df = read_csv("dataset3.csv", header=None)
model = create_model()

y_train = df.pop(9)
x_train = df

new_y_train = []
for y in y_train:
    _n = np.zeros((9,))
    _n[y] = 1
    new_y_train.append(_n)

y_train = np.array(new_y_train)

model.fit(x_train, y_train, epochs=100)
model.save("xo.h5")