from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
######################################################################################
# Smaller Regression datasets with less than 100k: Stochastic Gradient Descent
######################################################################################
# SGDRegressor
########################
x, y = make_regression(n_samples=1000, n_features=30)
print(x[0:2])
print(y[0:2])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=.15)

# Always scale the input. The most convenient way is to use a pipeline.
reg2 = make_pipeline(StandardScaler(),
                     SGDRegressor()
                     )
reg2.fit(xtrain, ytrain)
score = reg2.score(xtrain, ytrain)
print(score)





