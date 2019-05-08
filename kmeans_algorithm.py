# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:12:26 2019

@author: Gerardo Cervantes
"""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
import scipy
import numpy as np
from collections import Counter
import time

file_name = '10K_articles_each_20K features_3cats.npz'
file_name_dict = '10K_articles_each_dict.npy'
n_categories = 3
n_clusters = 8

ordered_labels = ['Conspiracy', 'Fake', 'Reliable']


dict_vocab_obj = np.load(file_name_dict)
dict_vocab = dict_vocab_obj.item()
print('Reading file...')
sparse_matrix = scipy.sparse.load_npz(file_name)
print('Done reading file')

articles_per_category = int(sparse_matrix.shape[0]/n_categories)

print('Clustering...')
start = time.time()
kmeans_algo = KMeans(n_clusters)
algo = kmeans_algo.fit(sparse_matrix)
print('Cluster run time: ' + str(time.time()-start))


cluster_labels = algo.labels_
counter = Counter(cluster_labels) #Find what are most common clusters assigned to.
most_common_tuple = counter.most_common()

article_labels = np.zeros(n_categories * articles_per_category, dtype = np.int)
for i, ordered_l in enumerate(ordered_labels):
    article_labels[articles_per_category*i:articles_per_category*(i+1)] = i
    
cluster_to_article_labels = np.zeros((n_clusters, n_categories))

for i, clust_label in enumerate(cluster_labels):
    cluster_to_article_labels[clust_label, article_labels[i]] += 1


cluster_centers = algo.__dict__['cluster_centers_']

score = silhouette_score(sparse_matrix, cluster_labels, metric = 'euclidean')
print("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))
#sample_silhouette_values = silhouette_samples(sparse_matrix, cluster_labels)

for i in range(n_clusters):
    
    clust_num, clust_freq = most_common_tuple[i]
    print('Cluster #' + str(clust_num) + ' with frequency ' + str(clust_freq))
    cluster_center = cluster_centers[clust_num]
    
    #Gets indices of the 15 highest correlated words
    high_corr_indices = sorted(range(len(cluster_center)), key=lambda i: cluster_center[i])[-15:]

        
    for i, article_label in enumerate(ordered_labels):
        print(article_label + ' ' + str(cluster_to_article_labels[clust_num, i]))
    corr_words = []
    for word, vocab_index in dict_vocab.items():
        if vocab_index in high_corr_indices:
            corr_words.append(word)
    print(corr_words)    
        