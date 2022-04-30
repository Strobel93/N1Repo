from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
######################################################################################
# Fist Attempt
# Principal Component Analysis (PCA)
######################################################################################
# Load Iris with 4 features (x)
iris = load_iris()
x = iris.data

# Reduce features from 4 to 3
pca = PCA(n_components=3)
pca.fit(x)
x_new = pca.transform(x)

# print(x_new)

# Reduce from Data estimation
pca2 = PCA(n_components='mle', svd_solver='full')
pca2.fit(x)
x_new2 = pca2.transform(x)

# print(x_new2)

from sklearn.datasets import load_iris
from sklearn.manifold import Isomap, SpectralEmbedding
######################################################################################
# ISOMAP: isometric mapping,
# Spectral Embedding
######################################################################################
# Reduce features from 4 to 3
iso = Isomap(n_components=3)
iso.fit(x)
new_x2 = iso.transform(x)

print(new_x2)

# Reduce features from 4 to 3
spec = SpectralEmbedding(n_components=3)
new_x3 = spec.fit_transform(x)
print(new_x3)
