import json
import logging

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ..utils import X_PATH, Y_PATH, MODEL_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    logger.info("Loading X.")
    with open(X_PATH, "r") as file:
        X = json.load(file)

    logger.info("Loading y.")
    with open(Y_PATH, "r") as file:
        y = json.load(file)

    logger.info("Instantiating model.")
    model = Pipeline(
        [("preprocessor", StandardScaler()), ("model", LogisticRegression())]
    )
    logger.info("Fitting model.")
    model.fit(X, y)

    logger.info("Saving model.")
    joblib.dump(model, MODEL_PATH)


if __name__ == "__main__":
    main()
