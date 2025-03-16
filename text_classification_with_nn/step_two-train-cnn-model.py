"""
model = tf.keras.models.Sequential([
		tf.keras.layers.Input(shape=(28,28,1)),
        tf.keras.layers.Conv2D(64, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Conv2D(64, (3,3), activation = "relu"),
        tf.keras.layers.MaxPooling2D(2,2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
])
"""
import utils as ut

from tensorflow.keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D

def load_dataset():
# load the vocabulary
    vocab = ut.load_doc('vocab.txt')
    vocab = set(vocab.split())
    
    docs, labels = ut.load_clean_dataset()
    
    return vocab, docs, labels

# fit a tokenizer
def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)

    return tokenizer

# integer encode and pad documents
def encode_docs(tokenizer, max_length, docs):
    # integer encode
    encoded = tokenizer.texts_to_sequences(docs)
    # pad sequences
    padded = pad_sequences(encoded, maxlen=max_length, padding='post')

    return padded

# define the model
def define_model(vocab_size, max_length):
    model = Sequential()
    model.add(Embedding(vocab_size, 100, input_length=max_length))
    model.add(Conv1D(32, 8, activation='relu'))
    model.add(MaxPooling1D())
    model.add(Flatten())
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # compile network
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # summarize defined model
#    model.summary()
#    plot_model(model, to_file='model.png', show_shapes=True)

    return model
    
def prepare_train_data(train_docs, max_length):
    # create the tokenizer
    tokenizer = create_tokenizer(train_docs)

    # encode data
    Xtrain = encode_docs(tokenizer, max_length, train_docs)
    
    return Xtrain, tokenizer 
    
# classify a review as negative or positive
def predict_sentiment(review, vocab, tokenizer, max_length, model):
    # clean review
    line = ut.clean_doc(review, vocab)
    # encode and pad review
    padded = encode_docs(tokenizer, max_length, [line])
    # predict sentiment
    yhat = model.predict(padded, verbose=0)

    # retrieve predicted percentage and label
    percent_pos = yhat[0,0]
    if round(percent_pos) == 0:
        return (1-percent_pos), 'NEGATIVE'
    return percent_pos, 'POSITIVE'

    
# load training data
vocab, train_docs, ytrain = load_dataset()
breakpoint()
# calculate the maximum sequence length
max_length = max([len(s.split()) for s in train_docs])
print('Maximum length: %d' % max_length)

Xtrain, tokenizer = prepare_train_data(train_docs, max_length)
# define vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary size: %d' % vocab_size)

# define model
model = define_model(vocab_size, max_length)

# fit network
model.fit(Xtrain, ytrain, epochs=10, verbose=2)

# test positive texts
ptext = ['Everyone will enjoy this film. I love it, recommended!', 'No bad, pretty entertaining.', 'Excellent']
for text in ptext: 
    percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_length, model)
    print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent*100))

# test negative text
ntext = ['This is a bad movie! Do not watch it. It sucks.', 'I was yonning all the time']
for text in ntext:
    percent, sentiment = predict_sentiment(text, vocab, tokenizer, max_length, model)
    print('Review: [%s]\nSentiment: %s (%.3f%%)' % (text, sentiment, percent*100))

# save the model
model.save('my_model.keras')


