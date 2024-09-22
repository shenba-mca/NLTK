# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import numpy as np
import pandas as pd
import random

# Load the dataset (replace with your own text file)
text = pd.read_csv("file.csv")

# Preprocess the text
words = word_tokenize(text)
words = [word.lower() for word in words]
word_set = set(words)

# Create a dictionary mapping words to integers
word_to_int = {word: i for i, word in enumerate(word_set)}
int_to_word = {i: word for word, i in word_to_int.items()}

# Prepare the training data
seq_len = 10
X = []
y = []

for i in range(len(words) - seq_len):
    seq = words[i:i + seq_len]
    label = words[i + seq_len]
    X.append([word_to_int[word] for word in seq])
    y.append(word_to_int[label])

# Convert data to numpy arrays
X = np.array(X)
y = np.array(y)

# One-hot encoding for labels
y = np_utils.to_categorical(y, num_classes=len(word_set))

# Define the RNN model
model = Sequential()
model.add(LSTM(64, input_shape=(seq_len, 1)))
model.add(Dropout(0.2))
model.add(Dense(len(word_set), activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, batch_size=128)

# Function to generate text
def generate_text(model, seed_text, seq_len, word_to_int, int_to_word):
    generated_text = seed_text
    for i in range(100): # Generate 100 words
        padded_seq = [word_to_int[word] for word in generated_text.split()[-seq_len:]]
        padded_seq = np.array(padded_seq).reshape(1, seq_len, 1)
        pred = model.predict(padded_seq, verbose=0)
        pred_word = int_to_word[np.argmax(pred)]
        generated_text += ' ' + pred_word
    return generated_text

# Test the text generation
seed_text = 'hello world'
generated_text = generate_text(model, seed_text, seq_len, word_to_int, int_to_word)
print(generated_text)