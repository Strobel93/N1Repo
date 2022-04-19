from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_iris
######################################################################################
# First and Second Prio
    # SGD Classifier
    # Kern Approximation
######################################################################################
# SGD Classifier
########################
iris = load_iris()

# Take first 2 features (relevant for distance calculation)
x = iris.data[:, :2]
y = iris.target

sgdc = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
sgdc.fit(x,y)

# print(sgdc.predict(x[-15:]))
# print(y[-15:])


########################
# Kernel Approximation
########################





