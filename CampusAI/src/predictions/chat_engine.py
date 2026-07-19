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
# Smart Response Selector
# -----------------------------
def select_response(intent_data, user_input):

    query = user_input.lower()

    # ---------- Library ----------
    if intent_data["intent"] == "library":

        if "timing" in query or "hour" in query:
            return "The library is open from 9:00 AM to 6:00 PM on all working days."

        elif "book" in query or "borrow" in query or "issue" in query:
            return "Students can borrow books using their library membership."

        elif "digital" in query:
            return "The college provides a digital library with online study resources."

        elif "rule" in query:
            return "Please contact the librarian for detailed library rules."

    # ---------- Hostel ----------
    elif intent_data["intent"] == "hostel":

        if "fee" in query:
            return "Hostel fee details are available at the hostel office."

        elif "room" in query:
            return "Hostel rooms are allotted based on availability."

        elif "facility" in query:
            return "Separate hostel facilities are available for boys and girls."

    # ---------- Fees ----------
    elif intent_data["intent"] == "fees":

        if "structure" in query:
            return "The latest fee structure is available on the official college website."

        elif "online" in query or "payment" in query:
            return "Students can pay fees online through the student portal."

    # ---------- Scholarship ----------
    elif intent_data["intent"] == "scholarship":

        if "eligibility" in query:
            return "Scholarship eligibility depends on college and government rules."

        elif "apply" in query or "form" in query:
            return "Students can apply through the official scholarship portal."

        elif "last date" in query:
            return "Please check the scholarship notice for the latest deadline."

    # ---------- Courses ----------
    elif intent_data["intent"] == "courses":

        if "b.tech" in query:
            return "The college offers B.Tech in multiple engineering branches."

        elif "mba" in query:
            return "MBA program is available."

        elif "mca" in query:
            return "MCA program is available."

        elif "department" in query:
            return "The college has Engineering, Management and Computer Application departments."

    # ---------- College Timings ----------
    elif intent_data["intent"] == "college_timings":

        if "timing" in query or "open" in query or "close" in query:
            return "College working hours are generally from 9:00 AM to 5:00 PM."

    # ---------- Placements ----------
    elif intent_data["intent"] == "placements":

        if "company" in query:
            return "Many reputed companies visit the campus during placement drives."

        elif "placement" in query:
            return "The Training and Placement Cell conducts placement activities every year."

    # ---------- Admission ----------
    elif intent_data["intent"] == "admission":

        if "online" in query:
            return "Students can apply online through the admission portal."

        elif "process" in query:
            return "Admission includes registration, document verification and fee payment."

        elif "document" in query:
            return "Required documents include marksheets, ID proof and photographs."

    # ---------- Greeting ----------
    elif intent_data["intent"] == "greeting":
        return random.choice(intent_data["responses"])

    # Default
    return random.choice(intent_data["responses"])


# -----------------------------
# Chat Response
# -----------------------------
def get_response(user_input):

    predicted_intent = predict_intent(user_input)

    for intent_data in knowledge_base:

        if intent_data["intent"] == predicted_intent:

            return select_response(intent_data, user_input)

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

        print("CampusAI :", get_response(user_input))