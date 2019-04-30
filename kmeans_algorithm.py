# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:12:26 2019

@author: Jerry C
"""

#import sklearn
from sklearn.cluster import KMeans, DBSCAN
import scipy
import json
import numpy as np
from collections import Counter
import random

file_name = 'reliable'
#DBSCAN()
kmeans_algo = KMeans(8)#, verbose = 1)

sparse_matrix = scipy.sparse.load_npz(file_name + '.npz')
dense_matrix = sparse_matrix.todense()
dense_matrix = dense_matrix[:1500, :]

#Normalize
#word_counts = np.sum(dense_matrix, axis = 1)
#dense_matrix = dense_matrix / word_counts[:, None]

#dense_matrix = dense_matrix  != 0
#dense_matrix = dense_matrix.astype(np.int8)
algo = kmeans_algo.fit(dense_matrix)

with open(file_name + '.json') as json_data:
    article_contents = json.load(json_data)

cluster_labels = algo.labels_
counter = Counter(cluster_labels) #Find what are most common clusters assigned to.
most_common_tuple = counter.most_common()
n_clusters_to_display = 8
examples_to_display = 2

for i in range(n_clusters_to_display):
    
    clust_num, clust_freq = most_common_tuple[i]
    print('Cluster # ' + str(clust_num))
    print('Cluster ' + str(clust_num) + ' with frequency ' + str(clust_freq))
    
    cluster_indices = np.where(cluster_labels == clust_num)[0]
    if examples_to_display <= len(cluster_indices):
        cluster_indices = random.sample(list(cluster_indices), examples_to_display)
    
    for j in range(examples_to_display):
        print('Random Article:')
        random_idx = random.choice(cluster_indices)
        random_article_in_cluster = article_contents[random_idx]
        print(random_article_in_cluster[:400] + '\n')