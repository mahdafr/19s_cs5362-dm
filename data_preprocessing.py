# -*- coding: utf-8 -*-
"""
Created on ~

@author: Gerardo Cervantes
"""
import argparse
import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
import string
import numpy as np
from collections import Counter
import os
import csv_const

import scipy

stop_words = set(stopwords.words('english'))
punctuation = string.punctuation + '“”’—–'


# returns list of lists of clean tokens
def clean_articles(article_contents):

    cleaned_article_contents = []

    for content in article_contents:
        content = content.lower()  # to lowercase
        content = content.translate(str.maketrans('', '', punctuation))  # remove punctuation
        tokens = nltk.word_tokenize(content)  # tokenize
        cleaned_content = [PorterStemmer().stem(token) for token in tokens if token not in stop_words]  # stem
        cleaned_article_contents.append(cleaned_content)

    return cleaned_article_contents


# create vocabulary dictionary (key is word, value is id) of size vocab_size
def create_vocab_dict(article_contents, vocab_size):
    words = [word for content in article_contents for word in content]
    vocab = Counter(words).most_common(vocab_size)           # [('cat', 13), ('inform', 10), ('cnn', 9), ...]
    vocab = [common_word[0] for common_word in vocab]        # ['cat', 'inform', 'cnn', ...]
    vocab = {key: value for value, key in enumerate(vocab)}  # {'cat': 0, 'inform': 1, 'cnn': 2, ...}
    return vocab


# Returns 2D matrix of size (nSamples, vocabSize) value is word frequency
def create_encoded_matrix(article_contents, vocab):
    vocab_size = len(vocab)
    articles_matrix = []
    for article in article_contents:
        article_vector = np.zeros(vocab_size, dtype=np.int8)
        for token in article:
            if token in vocab:
                article_vector[vocab[token]] += 1
        articles_matrix.append(article_vector)
    articles_matrix = np.array(articles_matrix)
    return articles_matrix


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='get matrix')
    parser.add_argument('-filename', type=str, required=True, help='.csv file')
    parser.add_argument('-article_limit', type=int, required=True, help='number of articles to read')
    parser.add_argument('-vocabulary_size', type=int, required=True, default=40000, help='number of words in vocabulary')
    args = parser.parse_args()

    filename_base = os.path.splitext(args.filename)[0]

    # default vocab size is 40k - too much and unknown words will show up

    csv.field_size_limit(2147483647)  # avoid errors on huge fields

    contents = []
    with open(args.filename, encoding=csv_const.ENCODING, newline=csv_const.NEWLINE) as csv_file:  # csv for reading
        reader = csv.reader(csv_file, delimiter=csv_const.DELIMITER)
        count = 0  # article limit could be more Pythonic...
        for row in csv.reader(csv_file, delimiter=csv_const.DELIMITER):
            fields = dict(zip(csv_const.FIELDS, row))
            contents.append(fields['content'])
            count += 1
            if count >= args.article_limit:
                break

    tokenized_articles = clean_articles(contents)  # clean and tokenize article contents
    vocabulary = create_vocab_dict(tokenized_articles, args.vocabulary_size)  # create vocabulary
    np.save('vocab_dict.npy', vocabulary)
    articles_matrix = create_encoded_matrix(tokenized_articles, vocabulary)  # convert to matrix
    sparse_matrix = scipy.sparse.csc_matrix(articles_matrix)  # convert to sparse matrix

    # save sparse matrix
    filename_base = os.path.splitext(args.filename)[0]
    scipy.sparse.save_npz(filename_base, sparse_matrix)

    # to load saved matrix file:
    # sparse_matrix = scipy.sparse.load_npz(file_name)
    # sparse_matrix.todense()
