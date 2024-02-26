import joblib
import numpy as np
from flask import Flask, request

from ..utils import MODEL_PATH

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health_check():
    model = joblib.load(MODEL_PATH)
    predict_proba = model.predict_proba(np.zeros((1, 3)))[:, 1].item()
    if predict_proba == 0.2979545043716624:
        return "Healthy", 200
    return "Unhealthy", 400


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    model = joblib.load(MODEL_PATH)
    return model.predict(data).tolist(), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
