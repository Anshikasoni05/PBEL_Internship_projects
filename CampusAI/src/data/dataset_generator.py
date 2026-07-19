import json
import pandas as pd
from pathlib import Path

from src.data.variation_generator import generate_variations

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

OUTPUT_PATH = (
    PROJECT_ROOT
    / "dataset"
    / "generated"
    / "generated_dataset.csv"
)

# -----------------------------
# Load Knowledge Base
# -----------------------------
def load_knowledge_base():
    with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# Create Dataset
# -----------------------------
def create_dataset():

    knowledge_base = load_knowledge_base()

    dataset = []

    for intent_data in knowledge_base:

        intent = intent_data["intent"]

        patterns = intent_data["patterns"]

        for pattern in patterns:

            variations = generate_variations(pattern)

            for variation in variations:

                dataset.append({
                    "text": variation,
                    "intent": intent
                })

    return dataset


# -----------------------------
# Save Dataset
# -----------------------------
def save_dataset(dataset):

    df = pd.DataFrame(dataset)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_PATH, index=False)

    print("\nDataset Generated Successfully!")

    print(f"Total Rows : {len(df)}")

    print(f"Saved At : {OUTPUT_PATH}")


# -----------------------------
# Main
# -----------------------------
def main():

    dataset = create_dataset()

    save_dataset(dataset)


if __name__ == "__main__":
    main()