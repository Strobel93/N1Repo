from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.cluster import v_measure_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
######################################################################################
# Clustering
    # less than 10k samples: MiniBatchKmeans
    # more than 10 samples: KMeans --> Spectral Clustering/GMM
######################################################################################
# Mini Batch K-Means
    # processes subsets of data in smaller batches
########################
categories = [
    "alt.atheism",
    "comp.graphics"
    ]
newsgroups = fetch_20newsgroups(subset="train", categories=categories)
kmeans = MiniBatchKMeans(n_clusters=len(categories), batch_size=20000, random_state=0)
vectorizer = TfidfVectorizer(stop_words="english", min_df=5)
x = vectorizer.fit_transform(newsgroups.data)
y = newsgroups.target

# print(newsgroups.keys())
# print(newsgroups.data[0])
# print(x[0])

# Fit Model
kmeans.fit(x)
clustering_result = kmeans.labels_
print(v_measure_score(clustering_result, y))


########################
# KMeans
########################
plt.figure(figsize=(12, 12))
n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# Incorrect number of clusters: top left
y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)

plt.subplot(221)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Incorrect Number of Blobs")

# Different variance (cluster_std): top right
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state)
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

plt.subplot(222)
plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
plt.title("Unequal Variance")

# Unevenly sized blobs(different sizes of subsets of data clusters): Bottom left
X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_filtered)

plt.subplot(223)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs")

plt.show()

from sklearn.cluster import SpectralClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from numpy import random
########################
# SpectralClustering
    # when center and spread around it is not a suitable way to describe cluster
    # creates similarity matrix, creates similarity by comparing  attributes/features individualy
########################
x, _ = make_blobs(n_samples=400, centers=4, cluster_std=1.5)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

sc = SpectralClustering(n_clusters=4)
sc.fit(x)
clustering_result = sc.labels_
plt.scatter(x[:, 0], x[:, 1], c=clustering_result)
plt.show()
