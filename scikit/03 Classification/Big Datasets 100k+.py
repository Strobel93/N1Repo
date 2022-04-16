from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
######################################################################################
# First Try/Attempts/Test (simplest/effective):
    # simplest /first algorithm for testing
######################################################################################
# Linear SVC
########################
x, y = load_iris(return_X_y=True)
pipe = make_pipeline(StandardScaler(),
                     LinearSVC())
x_train, x_test, y_train, y_test = train_test_split(x, y)
pipe.fit(x, y)

weights_assigned_to_n_features = pipe.named_steps['linearsvc'].coef_
constant_c_of_linear_formula = pipe.named_steps['linearsvc'].intercept_
# print(x_test[:5])
# print(pipe.predict(x_test[:5]))
# print(y_test[:5])
# print(weights_assigned_to_n_features)
# print(constant_c_of_linear_formula)

from sklearn.naive_bayes import GaussianNB
######################################################################################
# Text Data Analysis?
    # True: Naive Bayes
        # Complex example of text analysis with benchmark of multiple classifiers
        # https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py
    # False: KNeighbors Classifier / SVC
######################################################################################
# Naive Bayes: BASIC
########################
x, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y)

gnb = GaussianNB()
gnb.fit(x_train, y_train)

# print(x_test[:5])
# print(y_test[:5])
# print(gnb.predict(x_test[:5]))

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
########################
# Naive Bayes: Text
########################
# Get Text Data
data_train = fetch_20newsgroups(subset="train", categories=['sci.space'])
data_test = fetch_20newsgroups(subset="test", categories=['sci.space'])
print(data_train.keys())
print(data_train.data[0:5])

# Extracting features from the training/test data using a sparse vectorizer
# Converting Text into numerical (useable) form for model
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words="english")
x_train = vectorizer.fit_transform(data_train.data)
x_test = vectorizer.transform(data_test.data)

# split a training set and a test set
y_train, y_test = data_train.target, data_test.target

# print(x_train.shape)
# print(x_test.shape)
mnb = MultinomialNB()
mnb.fit(x_train, y_train)
pred = mnb.predict(x_test)
print('Score: ', accuracy_score(y_test, pred))

