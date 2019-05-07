# @author mahdafr
# @created apr2-19
# cs5362 project

import numpy as np
import random as rand
import json
from scipy.sparse import load_npz
from sklearn.cluster import DBSCAN
from sklearn import metrics

eps = 6
minPts = 1500
fdir = 'D:/dm_dataset/'
subset1 = '5K articles each, 20K features'
subset2 = '10K articles each, 20K features'
file = '30K articles each, 20K features'
subset3 = '60K articles each, 20K features'
fname = fdir + file + '.npz'

print('Running DBSCAN on file: ' + fname)
print('Using eps-value of: %0.2f' % eps)
print('Using minPts-value of: %d' % minPts)

# #############################################################################
# To load saved matrix file
sparse_matrix = load_npz(fname)
sparse_matrix.todense()

# To load saved json file
# with open(fdir + file + '.json') as json_data:
#     article_contents = json.load(json_data)

# #############################################################################
# Compute DBSCAN
X = sparse_matrix
db = DBSCAN(eps=eps, min_samples=minPts).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# True labels for each article
NUM_ARTICLES = labels.shape[0]
print('Number of articles: %d' % NUM_ARTICLES)
labels_true = np.zeros(shape=NUM_ARTICLES)
labels_true[:NUM_ARTICLES-1] = 1
labels_true[NUM_ARTICLES:2*NUM_ARTICLES-1] = 2
labels_true[2*NUM_ARTICLES:3*NUM_ARTICLES-1] = 3
labels_true[3*NUM_ARTICLES:] = 4

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

# print clusters info to file
clusters = set(labels)
file = open('_test.txt','a')
for i in range(db.components_.shape[0]):
    file.write(str(db.components_[i]) + '\n')
file.close()

# #############################################################################
# Results of DBSCAN and metrics
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
