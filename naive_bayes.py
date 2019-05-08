from sklearn.naive_bayes import GaussianNB

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
import numpy as np

import scipy

stop_words = set(stopwords.words('english'))
punctuation = string.punctuation + '“”’—–'


# returns list of clean tokens
def clean_article(content):
    content = content.lower()  # to lowercase
    content = content.translate(str.maketrans('', '', punctuation))  # remove punctuation
    tokens = nltk.word_tokenize(content)  # tokenize
    cleaned_content = [PorterStemmer().stem(token) for token in tokens if token not in stop_words]  # stem
    return cleaned_content


# Returns 2D matrix of size (nSamples, vocabSize) value is word frequency
def create_encoded_matrix(tokens, vocab):
    vocab_size = len(vocab)
    matrix = []

    article_vector = np.zeros(vocab_size, dtype=np.int8)
    for token in tokens:
        if token in vocab:
            article_vector[vocab[token]] += 1

    matrix.append(article_vector)
    matrix = np.array(matrix)
    return matrix


# load matrix
fake_dense = scipy.sparse.load_npz('fake.npz').todense()
reliable_dense = scipy.sparse.load_npz('reliable.npz').todense()

# assume vocab size for fake and reliable are equal
vocabulary_size = fake_dense.shape[1]

# read article content
# e.g. https://www.infowars.com/cnn-headline-asks-how-black-will-the-royal-baby-be/
with open('article.txt', encoding='utf-8') as f:
    article_content = f.read()

# get sparse matrix for article
article_tokens = clean_article(article_content)  # clean and tokenize article contents

vocabulary = np.load('vocab_dict.npz')
articles_matrix = create_encoded_matrix(article_tokens, vocabulary)  # convert to matrix
sparse_matrix = scipy.sparse.csc_matrix(articles_matrix)  # convert to sparse matrix
scipy.sparse.save_npz('article', sparse_matrix)

# load article matrix
article_dense = scipy.sparse.load_npz('article.npz').todense()

# if vocab size for article is less, fill with zeros
article_vocab_size = article_dense.shape[1]
if article_vocab_size < vocabulary_size:
    z = np.zeros((1, vocabulary_size - article_vocab_size), dtype=fake_dense.dtype)
    article_dense = np.concatenate((article_dense, z), axis=1)

# training_vectors = <concatenation of fake and reliable>
training_vectors = np.concatenate((fake_dense, reliable_dense), axis=0)

# target_values = [<number of fake articles> zeros <number of reliable> ones]
fake_n_articles = fake_dense.shape[0]
reliable_n_articles = reliable_dense.shape[0]
target_values = ([0] * fake_n_articles) + ([1] * reliable_n_articles)

classier = GaussianNB()
classier.fit(training_vectors, target_values)

print('fake = 0, reliable = 1')
print('article =', classier.predict(article_dense))
