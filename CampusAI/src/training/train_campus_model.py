import joblib
import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
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

MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Campus Dataset...")

df = pd.read_csv(DATASET_PATH)

print(f"Total Samples : {len(df)}")

X = df["text"]
y = df["intent"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Dataset Split Successfully!")

# -----------------------------
# TF-IDF
# -----------------------------
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),
    min_df=1
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

print("Text Vectorization Completed!")

# -----------------------------
# Model
# -----------------------------
model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

print("Training Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# -----------------------------
# Prediction
# -----------------------------
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nCampus Model Accuracy : {accuracy*100:.2f}%")

# -----------------------------
# Save
# -----------------------------
joblib.dump(model, MODEL_DIR / "campus_intent_model.pkl")
joblib.dump(vectorizer, MODEL_DIR / "campus_vectorizer.pkl")

print("\nCampus Model Saved Successfully!")