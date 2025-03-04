import numpy as np
import random
import tensorflow as tf

model = tf.keras.models.load_model('textgenerator.h5')

path = tf.keras.utils.get_file("poetry", "https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt")
text = open(path, 'rb').read().decode(encoding='utf-8')
text = text[300000:800000]
characters = sorted(set(text))
char_to_index = {char: index for index, char in enumerate(characters)}
index_to_char = {index: char for index, char in enumerate(characters)}
length = 40
size = 3


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generateText(length, temp):
    start = random.randint(0, len(text) - length - 1)
    generated = ''
    sentence = text[start : start + length]
    generated += sentence
    for i in range(length):
        x_pred = np.zeros((1, length, len(characters)), dtype = bool)
        for t , char in enumerate(sentence):
            x_pred[0, t, char_to_index[char]] = 1
            
        predictions = model.predict(x_pred, verbose = 0)[0]
        next_index = sample(predictions, temp)
        next_char = index_to_char[next_index]
        generated += next_char
        sentence = sentence[1:] + next_char
    return generated

print(generateText(300, 0.8))
        
        
    
    

