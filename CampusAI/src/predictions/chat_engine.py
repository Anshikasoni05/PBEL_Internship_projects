import json
import random
from pathlib import Path

from src.predictions.predict_intent import predict_intent

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]

KNOWLEDGE_BASE_PATH = (
    PROJECT_ROOT
    / "dataset"
    / "knowledge_base"
    / "knowledge_base.json"
)


# -----------------------------
# Load Knowledge Base
# -----------------------------
with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as file:
    knowledge_base = json.load(file)


# -----------------------------
# Get Response
# -----------------------------
def get_response(user_input):

    predicted_intent = predict_intent(user_input)

    for intent_data in knowledge_base:

        if intent_data["intent"] == predicted_intent:

            return random.choice(intent_data["responses"])

    return "Sorry, I couldn't understand your question."


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    print("CampusAI Chatbot (type 'exit' to quit)\n")

    while True:

        user_input = input("You : ")

        if user_input.lower() == "exit":
            break

        response = get_response(user_input)

        print("CampusAI :", response)