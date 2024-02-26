from pathlib import Path

ARTIFACT_DIR = Path("artifacts")
ARTIFACT_DIR.mkdir(exist_ok=True)

DATA_DIR = ARTIFACT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

MODEL_DIR = ARTIFACT_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

X_PATH = DATA_DIR / "X.json"
Y_PATH = DATA_DIR / "y.json"
MODEL_PATH = MODEL_DIR / "model.joblib"
