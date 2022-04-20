from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score
import numpy as np
######################################################################################
# Are all features relevant?
    # No: Lasso / ElasticNet
    # Yes: RidgeRegression, SVR(kernel='linear') --> SVR(kernel='rbf'), EnsembleRegressors
######################################################################################
# Not all Features are relevant
################################################
# Generate data with many features and y with decreasing coef --> simulating different impact of features
n_samples, n_features = 50, 100
X = np.random.randn(n_samples, n_features)

idx = np.arange(n_features)
coef = (-1) ** idx * np.exp(-idx / 10)
coef[10:] = 0  # sparsify coef
y = np.dot(X, coef)

# Add noise
y += 0.01 * np.random.normal(size=n_samples)

# Split data in train set and test set
n_samples = X.shape[0]
X_train, y_train = X[: n_samples // 2], y[: n_samples // 2]
X_test, y_test = X[n_samples // 2 :], y[n_samples // 2 :]

#######################
# Lasso and Elasticnet
#######################
# Lasso
lasso = Lasso()
y_pred_lasso = lasso.fit(X_train, y_train).predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(lasso)
print("r^2 on test data : %f" % r2_score_lasso)

# Elasticnet
enet = ElasticNet()
y_pred_enet = enet.fit(X_train, y_train).predict(X_test)
r2_score_enet = r2_score(y_test, y_pred_enet)
print(enet)
print("r^2 on test data : %f" % r2_score_enet)

from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.ensemble import VotingRegressor
################################################
# All Features are relevant
    # Prio 1: Ridge / SVR(kernel='linear')
    # Prio 2: SVR(kernel='rbf'), EnsembleRegressors (combine different results)
################################################
# Datasets
x, y = make_regression(n_samples=100, n_features=5)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.15)

# Ridge
ridge = Ridge()
ridge.fit(xtrain, ytrain)
print(ridge.score(xtest, ytest))

# SVR Linear
svr_lin = SVR(kernel='linear')
svr_lin.fit(xtrain, ytrain)
print(svr_lin.score(xtest, ytest))

# SVR RBF
svr_rbf = SVR(kernel='rbf')
svr_rbf.fit(xtrain, ytrain)
print(svr_rbf.score(xtest, ytest))

# VotingRegressor (combine different ML regresors and return avg)
svr_rbf = VotingRegressor(estimators=[('ridge', Ridge()), ('lin', SVR(kernel='linear')), ('rbf', SVR(kernel='rbf'))])
svr_rbf.fit(xtrain, ytrain)
print(svr_rbf.score(xtest, ytest))
