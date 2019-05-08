# @author mahdafr
# @created apr2-19
# cs5362 project

import numpy as np
from scipy.sparse import load_npz
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.metrics.pairwise import  pairwise_distances

eps = 70
minPts = -1
fdir = 'D:/dm_dataset/'
file2 = '5K articles each, 20K features'
file = '10K articles each, 20K features'
# subset2 = '30K articles each, 20K features'
# subset3 = '60K articles each, 20K features'
fname = fdir + file + '.npz'

# #############################################################################
# To load saved matrix file
sparse_matrix = load_npz(fname)
sparse_matrix.todense()

# To load saved json file
# with open(fdir + file + '.json') as json_data:
#     article_contents = json.load(json_data)

# #############################################################################
# Compute DBSCAN
print('Running DBSCAN on file: ' + fname)
print('Using eps-value of: %0.2f' % eps)
print('Using minPts-value of: %d' % minPts)
X = sparse_matrix
db = DBSCAN(eps=eps).fit(X)  # eps=eps, min_samples=minPts).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# True labels for each article
NUM_ARTICLES = labels.shape[0]
print('Number of articles: %d' % NUM_ARTICLES)
labels_true = np.zeros(shape=NUM_ARTICLES)
labels_true[:round(NUM_ARTICLES/3)-1] = 1  # conspiracy
labels_true[round(NUM_ARTICLES/3):2*round(NUM_ARTICLES/3)-1] = 2  # fake
labels_true[2*round(NUM_ARTICLES/3):3*round(NUM_ARTICLES/3)-1] = 3  # reliable
# labels_true[3*NUM_ARTICLES:] = 4  # unreliable

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

# print clusters info to file
print('Printing results to file')
# file = open('RES_COMPONENTS.txt','a')
# for i in range(db.components_.shape[0]):
#     file.write(str(db.components_[i]) + '\n')
# file.close()
# file = open('RES_SAMPLE-INDICES.txt','a')
# for i in range(db.core_sample_indices_.shape[0]):
#     file.write(str(db.core_sample_indices_[i]) + '\n')
# file.close()
nfile = open('RES_NOISE_eps=' + str(eps) + '_minPts=' + str(minPts) + '.txt', 'a')
nfile.write('NOISE: \n')
for i in range(db.labels_.shape[0]):
    if db.labels_[i] == -1:
        nfile.write(str(i) + '\n')
nfile.close()

lfile = open('RES_LABELS_eps=' + str(eps) + '_minPts=' + str(minPts) + '.txt', 'a')
for lab in range(n_clusters_):
    lfile.write('LABEL: ' + str(lab) + '\n')
    lst = db.labels_ == lab
    for i in range(lst.shape[0]):
        if lst[i]:
            lfile.write(str(i) + '\n')
lfile.close()

dmfile = open('RES_DIST-MATRIX_eps=' + str(eps) + '_minPts=' + str(minPts) + '.txt', 'a')
dist_matr = pairwise_distances(X)
for point in range(db.core_sample_indices_ .shape[0]):
    distances = []
    for clust in range(n_clusters_):
        distance = dist_matr[point, clust].min()  # Single linkage
        distances.append(distance)
    dmfile.write("The cluster for {} is {}".format(point, clust))
    dmfile.write('\n')
dmfile.close()

# #############################################################################
# Results of DBSCAN and metrics
noiseRat = n_noise_/NUM_ARTICLES
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print('Noise/Clustered Ratio: %0.3f' % noiseRat)
# print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
# print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
# print("V-measure: %0.2f" % metrics.v_measure_score(labels_true, labels))
# print("Adjusted Rand Index: %0.5f" % metrics.adjusted_rand_score(labels_true, labels))
# print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
