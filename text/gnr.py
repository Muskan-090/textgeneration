import tensorflow as tf
import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

def txtgen(txt):
    text = open('C://Users//user//Desktop//MS//Scraping//textgeneration//text//book.txt', 'r', 
    encoding='utf-8').read()
    text = text.lower()

    #create list of sentences
    sentences = text.split('\n')

    tokenizer = Tokenizer(oov_token='<UNK>')
    tokenizer.fit_on_texts(sentences)

    vocab_size = len(tokenizer.word_index) + 1

    sequences = tokenizer.texts_to_sequences(sentences)

    input_sequences = []
    for sequence in sequences:
        for i in range(1, len(sequence)):
            n_gram_sequence = sequence[:i+1]
            input_sequences.append(n_gram_sequence)

    max_seq_len = max([len(seq) for seq in input_sequences])
    padded_sequences = pad_sequences(input_sequences, maxlen = max_seq_len)


    padded_sequences = np.array(padded_sequences)

    x = padded_sequences[:, : -1]
    labels = padded_sequences[:, -1]

    y = tf.keras.utils.to_categorical(labels, num_classes=vocab_size)


    model = Sequential()
    model.add(Embedding(vocab_size, 100, input_length=max_seq_len-1))
    model.add(Bidirectional(LSTM(256)))
    model.add(Dense(vocab_size, activation='softmax'))
    adam = Adam(learning_rate=0.01)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['acc'])

    from tensorflow.keras.callbacks import EarlyStopping
    es = EarlyStopping(monitor = 'acc', min_delta=0.03)

    model.fit(x, y, epochs=10, verbose=1, batch_size=512)

    seed_text = str(txt  )      
    next_words = 100
    
    for _ in range(next_words):
        sequence = tokenizer.texts_to_sequences([seed_text])
        padded = pad_sequences(sequence, maxlen=max_seq_len-1)
        predicted = np.argmax(model.predict(padded, verbose=0))
        output_word = ''
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += ' ' + output_word
    print(seed_text)
    return seed_text