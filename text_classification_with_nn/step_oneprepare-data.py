"""
this script reads reviews from two directories: text_pos and text_neg.
data preparations are done in 2 steps:
1) prepare vocab.txt - a set of all meaningful words that appear in reviews
2) prepare dataset.csv - a list of labeled reviews with all low meaningful terms removed
"""
import re
import string

import utils as ut


def prepare():
    # prepare regex for char filtering
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))

    # create vocabulary of all words and make list of all texts
    vocab = ut.make_vocab(re_punc)
    # print the size of the vocab
    print(f"Vocabulary size: {len(vocab)}")

    # add all docs to vocab
    pos_docs = ut.process_docs('text_pos', vocab, re_punc, True)
    neg_docs = ut.process_docs('text_neg', vocab, re_punc, True)

    # keep tokens with a min occurrence
    min_occurrence = 2
    tokens = [k for k, c in vocab.items() if c >= min_occurrence]
    print(f"Total tokens: {len(tokens)}")

    # print the top words in the vocab
    print(f"Most common: {vocab.most_common(50)}")

    # save tokens to a vocabulary file
    ut.save_list(tokens, 'vocab.txt')
    print("Vocabulary is saved...")

    ut.make_clean_dataset(vocab, neg_docs, pos_docs)


if __name__ == '__main__':
    prepare()
