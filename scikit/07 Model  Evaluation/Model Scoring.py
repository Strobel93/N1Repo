from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import r2_score, accuracy_score
######################################################################################
# Evaluation: 01 General for multiple executions
# CV = Cross Validation = Execute and Split N Times with different test_train splits
######################################################################################
# Data and Model
x, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
model = SVC().fit(x_train, y_train)
y_pred = model.predict(x_test)

# Scoring:
    # R2 = regression (continous data)
    # accuracy = classification
sing_score = model.score(x_test, y_test)
scores_for_each_cv_iter = cross_val_score(model, x, y, cv=5)
# r2_regression_score = r2_score(x_test, y_test)
acc_score = accuracy_score(y_pred, y_test)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
#########################################################################################
# Running Multiple Models:
# scoring = define mathematical scoring strategy
#########################################################################################
X_train = X_test = y_train = y_test = 0
names = []
predictions = []
scoring = ['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted', 'roc_auc']
models = [
    ('LogReg', LogisticRegression()),
    ('RF', RandomForestClassifier()),
    ('KNN', KNeighborsClassifier()),
    ('SVM', SVC()),
    ('GNB', GaussianNB()),
]

for name, model in models:
    # Set up 5 different train/test splits of same data
    k_fold = model_selection.KFold(n_splits=5, shuffle=True, random_state=90210)
    # Cross Validate the current model using different/multiple scoring systems
    cv_results = model_selection.cross_validate(model, X_train, y_train, cv=k_fold, scoring=scoring)
    # Train Model and Predict values (optional?)
    clf = model.fit(X_train, y_train)
    y_predicts = clf.predict(X_test)

    # Append Results: Scores and Predictions
    predictions.append([name, y_predicts])
    names.append([name, cv_results])