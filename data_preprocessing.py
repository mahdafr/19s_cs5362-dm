# -*- coding: utf-8 -*-
"""
Created on ~

@author: Gerardo Cervantes
"""

import json
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
import numpy as np
import scipy

# Tokenizes the articles, and cleans the input
# Returns list of lists of size (nArticles, nWordsInArticle)
def clean_articles(article_contents):
    ps = PorterStemmer()
    # lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    cleaned_article_contents = []
    for content in article_contents:
        content = content.rstrip('\n')  # removes \n
        # Efficient way to remove punctuation
        content = content.translate(str.maketrans('', '', string.punctuation))
        content = content.lower()  # lowercase
        tokens = nltk.word_tokenize(content)
        cleaned_content = [ps.stem(w) for w in tokens if not w in stop_words]
        # lemmatized_word = lemmatizer.lemmatize(word)
        cleaned_article_contents.append(cleaned_content)
    return cleaned_article_contents


# Creates a vocabulary (dictionary-key is word, value is id) of size vocab_size.
# TODO could be improved by looking for most common words, for purposes of clustering, it will have little affect
def create_vocab_dict(article_contents, vocab_size):
    vocab = {}
    word_id = 0
    for article in article_contents:
        for token in article:

            if token not in vocab:
                # Add to vocab and increment id #
                vocab[token] = word_id
                word_id += 1
                if vocab_size <= word_id:
                    return vocab
    return vocab


# Returns 2D matrix of size (nSamples, vocabSize) value is word frequency
def create_one_hot_encoded_matrix(article_contents, vocab):
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
    file_name = 'fake'
    data_path = 'D:/dm_dataset/' + file_name + '.json'

    with open(data_path) as json_data:
        conts = json.load(json_data)
    article_contents = conts[:15000] # 30000, 50000, 70000, 80000
    print('Finished reading JSON file')
    vocab_size = 20000 # 40k is a good size - too much and unknown words will show up
    tokenized_articles = clean_articles(conts)
    print('Finish cleaning and tokenizing articles')
    vocab = create_vocab_dict(tokenized_articles, vocab_size)
    print('Created vocab of size ' + str(vocab_size))
    articles_matrix = create_one_hot_encoded_matrix(tokenized_articles, vocab)
    np.save(file_name + '_dict.npy', vocab)
    print('Finished converting articles to a matrix')
    sparse_matrix = scipy.sparse.csc_matrix(articles_matrix)
    print('Converted to sparse')
    scipy.sparse.save_npz(file_name, sparse_matrix)
    print('Saved matrix to file')
    # To load saved matrix file:
    # sparse_matrix = scipy.sparse.load_npz(file_name)
    # sparse_matrix.todense()
