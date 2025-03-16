import string
import re
from os import listdir
from numpy import array
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords


# load doc into memory
def load_doc(filename: str) -> str:
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    #    nltk.download('stopwords')

    return text


# turn a doc into clean tokens
def clean_doc(doc: str, vocab: set, re_punc: object) -> str:
    # split into tokens by white space
    tokens = doc.split()
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]

    # filter out tokens not in vocab
    tokens = [w for w in tokens if w in vocab]
    tokens = ' '.join(tokens)

    return tokens


# load doc and add to vocab
def add_to_vocab(doc: str, vocab: set, re_punc: object) -> list:
    # load doc
    tokens = doc.split()
    # remove punctuation from each word
    tokens = [re_punc.sub('', w) for w in tokens]
    # remove remaining tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]

    return tokens


# save list to file
def save_list(lines: list, filename: str) -> None:
    # convert lines to a single blob of text
    data = '\n'.join(lines)
    # open file
    file = open(filename, 'w')
    # write text
    file.write(data)
    # close file
    file.close()


def make_vocab(re_punc: object) -> set:
    vocab = Counter()
    for fldr in ['text_neg', 'text_pos']:
        for filename in listdir(fldr):
            # create the full path of the file to open
            path = fldr + '/' + filename
            # load the doc
            doc = load_doc(path)
            # clean doc
            tokens = add_to_vocab(doc, vocab, re_punc)
            # add to Counter
            vocab.update(tokens)

    return vocab


# load all docs in a directory
def process_docs(directory: str, vocab: set, re_punc: object, is_train: bool)-> list:
    documents = list()
    # walk through all files in the folder
    for filename in listdir(directory):
        # skip any reviews in the test set
        if is_train and filename.startswith('cv9'):
            continue
        if not is_train and not filename.startswith('cv9'):
            continue
        # create the full path of the file to open
        path = directory + '/' + filename
        # load the doc
        doc = load_doc(path)
        # clean doc
        tokens = clean_doc(doc, vocab, re_punc)
        # add to list
        documents.append(tokens)

    return documents


# load and clean a dataset
def load_clean_dataset() -> tuple:
    ds = pd.read_csv('dataset.csv')
    docs = ds['Docs'].tolist()
    labels = ds['Labels'].tolist()

    return docs, labels


# load training texts from file    
def make_clean_dataset(vocab: set, neg: list, pos: list) -> None:
    docs = neg + pos

    # prepare labels
    labels = array([0 for _ in range(len(neg))] + [1 for _ in range(len(pos))])

    ds = pd.DataFrame(columns=['Docs', 'Labels'])
    ds['Docs'] = docs
    ds['Labels'] = labels

    ds.to_csv('dataset.csv')
    print('All texts are saved...')


if __name__ == '__main__':
    main()
