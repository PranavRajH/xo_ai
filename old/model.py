from keras import layers, Sequential

import numpy as np

def create_model():
    model = Sequential()

    model.add(layers.Flatten(input_shape=(9,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(9, activation='softmax'))

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
    
    return model


def train_model(model: Sequential, x_train, y_train):
    for x,y in zip(x_train, y_train):
        y = np.array([1 if(i!=0) else 0 for i in (y.reshape((9,)) - x.reshape((9,)))])
        model.fit(x.reshape(1,9), y.reshape(1,9), epochs=50, verbose=0)
    return model