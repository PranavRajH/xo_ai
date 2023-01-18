from tensorflow.keras import layers, models, Sequential
from pickle import dump, load

import numpy as np

def create_model():
    model = Sequential()

    model.add(layers.Flatten(input_shape=(3,3)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(9, activation='softmax'))

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
    
    return model


def save_model(model: Sequential):
    with open("model.bin", "wb") as file:
        dump(model, file)


def load_model():
    with open("model.bin", "rb") as file:
        return load(file)


def train_model(model: Sequential, x_train, y_train):
    for x,y in zip(x_train, y_train):
        y = np.array([1 if(i!=0) else 0 for i in (y.reshape((9,)) - x.reshape((9,)))])
        model.fit(x.reshape(1,3,3), y.reshape(1,9), epochs=10, verbose=0)
    