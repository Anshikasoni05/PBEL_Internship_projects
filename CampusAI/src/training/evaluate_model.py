import joblib
import pandas as pd
from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.model_selection import train_test_split

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET_PATH = (
    PROJECT_ROOT
    / "dataset"
    / "generated"
    / "generated_dataset.csv"
)

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "campus_intent_model.pkl"
)

VECTORIZER_PATH = (
    PROJECT_ROOT
    / "models"
    / "campus_vectorizer.pkl"
)

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Dataset...\n")

df = pd.read_csv(DATASET_PATH)

X = df["text"]
y = df["intent"]

# -----------------------------
# Same Split as Training
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Load Saved Model
# -----------------------------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# -----------------------------
# Transform Test Data
# -----------------------------
X_test_vectorized = vectorizer.transform(X_test)

# -----------------------------
# Prediction
# -----------------------------
predictions = model.predict(X_test_vectorized)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

print("=" * 60)
print(f"CampusAI Model Accuracy : {accuracy*100:.2f}%")
print("=" * 60)

# -----------------------------
# Classification Report
# -----------------------------
print("\nClassification Report\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

# -----------------------------
# Confusion Matrix
# -----------------------------
print("\nConfusion Matrix\n")

print(
    confusion_matrix(
        y_test,
        predictions
    )
)