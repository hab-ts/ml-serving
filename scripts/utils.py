from pathlib import Path

ARTIFACT_DIR = Path("artifacts")
DATA_DIR = ARTIFACT_DIR / "data"
MODEL_DIR = ARTIFACT_DIR / "models"

X_PATH = DATA_DIR / "X.json"
Y_PATH = DATA_DIR / "y.json"
MODEL_PATH = MODEL_DIR / "model.joblib"
