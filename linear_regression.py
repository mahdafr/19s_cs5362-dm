# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:09:42 2019

@author: Gerardo Cervantes
"""

import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
import scipy
import time

#Shuffles X and Y
def unison_shuffled_copies(a, b):
    p = np.random.permutation(len(b))
    return a[p], b[p]

file_name = '10K_articles_each_20K features_3cats.npz'
file_name_dict = '10K_articles_each_dict.npy'

n_articles = 20000
ordered_labels = ['Conspiracy', 'Fake', 'Reliable']
threshold = 0.5

dict_vocab_obj = np.load(file_name_dict)
dict_vocab = dict_vocab_obj.item()

print('Reading file...')
sparse_matrix = scipy.sparse.load_npz(file_name)
sparse_matrix = sparse_matrix[10000:, :]
print('Done reading file')

#Create labels
labels = np.zeros((n_articles), dtype = np.int)
labels[int(n_articles/2):] = 1

sparse_matrix, labels = unison_shuffled_copies(sparse_matrix, labels)

train_split = 0.75
x_train = sparse_matrix[:int(n_articles*train_split),:]
y_train = labels[:int(n_articles*train_split)]
x_test = sparse_matrix[int(n_articles*train_split):,:]
y_test = labels[int(n_articles*train_split):]

print('Linear regression...')
start = time.time()
reg = LinearRegression().fit(x_train, y_train)
train_pred = reg.predict(x_train)
train_acc = sklearn.metrics.accuracy_score(y_train, train_pred > threshold)
print('Train score:' + str(train_acc))

test_pred = reg.predict(x_test)
test_acc = sklearn.metrics.accuracy_score(y_test, test_pred > threshold)
print('Test score:' + str(test_acc))

print('Linear Regression run time: ' + str(time.time()-start))

