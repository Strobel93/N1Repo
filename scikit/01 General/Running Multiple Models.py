from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection
#########################################################################################
# Running Multiple Models
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
