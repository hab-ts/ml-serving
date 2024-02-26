import json

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ..utils import X_PATH, Y_PATH, MODEL_PATH


def main():
    with open(X_PATH, "r") as file:
        X = json.load(file)
    with open(Y_PATH, "r") as file:
        y = json.load(file)

    model = Pipeline([("preprocessor", StandardScaler()), ("model", LogisticRegression())])
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    main()
