import json
import logging

from sklearn.datasets import make_classification

from ..utils import X_PATH, Y_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    logger.info("Making dataset.")
    X, y = make_classification(
        n_samples=10,
        n_features=3,
        n_informative=2,
        n_redundant=1,
        n_classes=2,
        random_state=0,
    )

    logger.info("Saving X.")
    with open(X_PATH, "w") as file:
        json.dump(X.tolist(), file)

    logger.info("Saving y.")
    with open(Y_PATH, "w") as file:
        json.dump(y.tolist(), file)


if __name__ == "__main__":
    main()
