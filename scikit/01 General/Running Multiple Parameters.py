from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
#########################################################################################
# GridSearchCV(model, parameters) --> execute model with different list of parameters
#########################################################################################
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svc = svm.SVC()
clf = GridSearchCV(svc, parameters)


clf.fit(iris.data, iris.target)
sorted(clf.cv_results_.keys())





