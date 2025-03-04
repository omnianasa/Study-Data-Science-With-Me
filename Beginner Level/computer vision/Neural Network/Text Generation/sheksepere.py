import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, LSTM
from tensorflow.keras.optimizers import RMSprop

#preparing the data
path = tf.keras.utils.get_file("poetry", "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")
text = open(path, 'rb').read().decode(encoding='utf-8')

characters = sorted(set(text))

char_to_index = {char: index for index, char in enumerate(characters)}
index_to_char = {index: char for index, char in enumerate(characters)}

length = 40
size = 3
sentences = []
next_char = []

for i in range(0, len(text) - length, size):
    sentences.append(text[i:i+length])
    next_char.append(text[i+length])
   
x = np.zeros((len(sentences), length, len(characters)), dtype= bool)
y = np.zeros((len(sentences), len(characters)), dtype= bool)

for i, satz in enumerate(sentences):
    
    for t, char in enumerate(satz):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[next_char[i]]] = 1
    

# Building the neural network
model = Sequential()
model.add(LSTM(128, input_shape=(length, len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = RMSprop(learning_rate = 0.01))
model.fit(x, y, batch_size = 256, epochs = 4)
model.save('textgenerator.h5')



    


