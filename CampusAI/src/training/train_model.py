from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "models"
MODEL_DIR.mkdir(exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
print("Loading Dataset...")

dataset = load_dataset("Mozilla/smart_intent_dataset")

df = dataset["train"].to_pandas()

X = df["sequence"]
y = df["target"]

print(f"Total Samples : {len(df)}")

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Dataset Split Completed")

# -----------------------------
# TF-IDF Vectorizer
# -----------------------------
vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

print("Text Vectorization Completed")

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000)

print("Training Started...")

model.fit(X_train_vectorized, y_train)

print("Training Completed!")

# -----------------------------
# Prediction
# -----------------------------
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy : {accuracy*100:.2f}%")

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, MODEL_DIR / "intent_model.pkl")
joblib.dump(vectorizer, MODEL_DIR / "vectorizer.pkl")

print("\nModel Saved Successfully!")