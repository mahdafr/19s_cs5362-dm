# @author mahdafr
# @created apr2-19
# cs5362 project

import numpy as np
from scipy.sparse import load_npz
from sklearn.cluster import DBSCAN
from sklearn import metrics

eps = 0.9
minPts = 10
subset = 'reliable'
fname = 'D:/dm_dataset/' + subset + '.npz'

print('Running DBSCAN on subset: ' + subset)
print('Using eps-value of: %0.2f' % eps)
print('Using minPts-value of: %d' % minPts)

# #############################################################################
# To load saved matrix file
sparse_matrix = load_npz(fname)
sparse_matrix.todense()

# #############################################################################
# Compute DBSCAN
X = sparse_matrix
print('The size of ' + subset + ' is: %d' % X.shape[0])
db = DBSCAN(eps=eps, min_samples=minPts).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))
