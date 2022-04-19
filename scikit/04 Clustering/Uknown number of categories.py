from sklearn.datasets import make_blobs
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.datasets import load_iris
from sklearn.mixture import BayesianGaussianMixture
######################################################################################
# Clustering for less than 10k Samples
    # MeanShift = centroids = mean of points in given region
    # VBGMM (Variational Bayesian Gaussian Mixture) =
######################################################################################
# MeanShift
########################
# Generate Sample Data: 2 Dimensional Data with n Rows witg 3 centers
x, _ = make_blobs(n_samples=1000, centers=3, cluster_std=0.6)
ms = MeanShift()
ms.fit(x)
# Results
cluster_assignments_for_results= ms.labels_
cluster_locations = ms.cluster_centers_
centers = set(ms.labels_)

# Plot result
plt.figure(1)
plt.clf()

colors = cycle("bgrcmykbgrcmykbgrcmykbgrcmyk")
# for each center ( 3 centers --> 0,1,2)
for k, col in zip(range(len(centers)), colors):
    # get True for each dataset with matching center
    my_members = cluster_assignments_for_results == k
    # get all x values by first and second index, matching my_member entries/rows
    # plotting only those of current center
    plt.plot(x[my_members, 0], x[my_members, 1], col + ".")
plt.title("Estimated number of clusters: %d" % len(centers))
# plt.show()



########################
# VBGMM
########################
iris = load_iris()

# Take first 2 features (relevant for distance calculation)
x = iris.data[:, :2]
y = iris.target

# Model with (components can be thought of as the k of k-means)
vbgmm = BayesianGaussianMixture(n_components=2)
vbgmm.fit(x)

print(x[0:3], '\n')
print(y[0:3], '\n')
print(vbgmm.predict(x[0:3]), '\n')
print(vbgmm.means_)
print(vbgmm.covariances_)
