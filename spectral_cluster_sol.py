from scipy.io import loadmat
from sklearn.cluster import SpectralClustering
import numpy as np
from sklearn.metrics.cluster import supervised
from scipy.optimize import linear_sum_assignment

data = loadmat('../digits/digits-train.mat')

# data = loadmat('../objects/objects-train.mat')

#fea_hog = np.array(data['fea_hog_train'])

fea_hog = np.array(data['fea_scat_train'])

labels = np.array(data['labels_train']).flatten()

print(labels.shape)

print(fea_hog.transpose().shape)

#test_gamma = [.5,.55,.6,.65,.7,.75,.8,.85,.9,.95,1]
test_gamma = [.1,.15,.2,.25,.3,.35,.4,.45]
#test = [1,2,3,4,5,6,7,8,9,10]

#for x in test_gamma:
spec_clust = SpectralClustering(n_clusters=5,affinity='nearest_neighbors',n_neighbors=3).fit(fea_hog.transpose())

#print(spec_clust.get_params())

labels_pred = np.array(spec_clust.labels_)

#print(labels_pred.shape)

labels, labels_pred = supervised.check_clusterings(labels, labels_pred)
# labels_true : int array with ground truth labels, shape = [n_samples]
# labels_pred : int array with estimated labels, shape = [n_samples]
value = supervised.contingency_matrix(labels, labels_pred)
# value : array of shape [n, n] whose (i, j)-th entry is the number of samples in true class i and in predicted class j
[r, c] = linear_sum_assignment(-value)
accr = value[r, c].sum() / len(labels)
print(accr)
#print('gamma: ' + str(x) + ' accr: ' + str(accr))

# for x in range(0,20):
#     print(kmeans.labels_[x])

# for x in range(0,10):
#     print(data['fea_hog_train'][x])
