import logging

import joblib
import numpy as np
from flask import Flask, request

from ..utils import MODEL_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    logger.info("Checking health...")

    logger.info("Loading model.")
    model = joblib.load(MODEL_PATH)

    logger.info("Predicting probability.")
    predict_proba = model.predict_proba(np.zeros((1, 3)))[:, 1].item()

    logger.info("Checking result.")
    if predict_proba == 0.2979545043716624:
        logger.info("Health check successful.")
        return "Healthy", 200

    logger.info("Health check unsuccessful.")
    return "Unhealthy", 400


@app.route("/predict", methods=["POST"])
def predict():
    logger.info("Predicting...")

    logger.info("Getting data.")
    data = request.get_json()

    logger.info("Loading model.")
    model = joblib.load(MODEL_PATH)

    logger.info("Predicting.")
    prediction = model.predict(data).tolist()

    logger.info("Prediction successful.")
    return prediction, 200


if __name__ == "__main__":
    logger.info("Initialising app...")
    app.run(host="0.0.0.0", port=8080)
    logger.info("Closing app.")
