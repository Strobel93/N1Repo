from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
#########################################################################################
# Parameter Optimization/Tuning
# GridSearchCV(model, parameters): slower, because tries all possible parameter permutations given
# RandomizedSearchCV(model, parameters): faster, randomized combinations, execution number = number of permutations
    # execute model with different list of parameters
    # faster execution versions (HalvingGridSearchCV and HalvingRandomSearchCV)
    # c = hyperparamter for regulariztation --> penalty for outliers --> to balance over/underfitting
        # small c = dont "trust" training data (penalizing)
        # big c   = "trust" training data
#########################################################################################
# Classifier Model and Data for parameters: Kernel +
iris = datasets.load_iris()
parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10, 100, 150, 300]}
svc = svm.SVC()

# Search: Search(Model_or_Pipe, parameters)
# GridSearchCV
clf = GridSearchCV(svc, parameters)
clf.fit(iris.data, iris.target)
print(sorted(clf.cv_results_.keys()))
print(clf.best_params_)
# RandomizedSearchCV
clf2 = RandomizedSearchCV(svc, parameters, n_iter= 20)
clf2.fit(iris.data, iris.target)
print(clf2.best_params_)



