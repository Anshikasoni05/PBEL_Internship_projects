import joblib
from pathlib import Path

from src.data.preprocess import clean_text

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "campus_intent_model.pkl"
VECTORIZER_PATH = PROJECT_ROOT / "models" / "campus_vectorizer.pkl"

# -----------------------------
# Load Model Once
# -----------------------------
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_intent(user_input):
    """
    Predict the intent of user query.
    """

    cleaned_text = clean_text(user_input)

    vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(vector)[0]

    return prediction


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    while True:

        question = input("\nYou : ")

        if question.lower() == "exit":
            break

        intent = predict_intent(question)

        print("Predicted Intent :", intent)