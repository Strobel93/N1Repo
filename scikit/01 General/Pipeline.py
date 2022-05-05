from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
#########################################################################################
# Pipeline: do all in one step: list of datatransformations on data + one model
#########################################################################################
x = y = x2 = 0
model_pipeline = make_pipeline(StandardScaler(), VarianceThreshold(), KNeighborsClassifier())
model_pipeline = Pipeline([
                                    ('scaler', StandardScaler()),
                                    ('selector', VarianceThreshold()),
                                    ('classifier', KNeighborsClassifier())
                        ])
model_pipeline.fit(x, y)
model_pipeline.predict(x2)

# Access steps:
model_pipeline[0]
model_pipeline['scaler']


