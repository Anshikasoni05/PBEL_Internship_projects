import json
import random
import pandas as pd
from pathlib import Path

from src.utils.synonyms import SYNONYMS
# Project Paths
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
def load_knowledge_base():
    """
    Load the knowledge base from JSON file.
    """

    with open(KNOWLEDGE_BASE_PATH, "r", encoding="utf-8") as file:
        knowledge_base = json.load(file)

    return knowledge_base
def generate_variations(question):
    """
    Generate different variations of a question
    using the custom synonym dictionary.
    """

    variations = set()

    # Original question
    variations.add(question)

    words = question.lower().split()

    for i, word in enumerate(words):

        clean_word = word.strip("?,.!")

        if clean_word in SYNONYMS:

            for synonym in SYNONYMS[clean_word]:

                new_words = words.copy()

                new_words[i] = synonym

                new_sentence = " ".join(new_words)

                variations.add(new_sentence.capitalize())

    return list(variations)
def create_dataset():
    """
    Create dataset from knowledge base.
    """

    knowledge_base = load_knowledge_base()

    dataset = []

    for intent, questions in knowledge_base.items():

        for item in questions:

            question = item["question"]

            variations = generate_variations(question)

            for variation in variations:

                dataset.append(
                    {
                        "text": variation,
                        "intent": intent
                    }
                )

    return dataset
def create_dataset():
    """
    Create dataset from knowledge base.
    """

    knowledge_base = load_knowledge_base()

    dataset = []

    for intent, questions in knowledge_base.items():

        for item in questions:

            question = item["question"]

            variations = generate_variations(question)

            for variation in variations:

                dataset.append(
                    {
                        "text": variation,
                        "intent": intent
                    }
                )

    return dataset
def save_dataset(dataset):
    """
    Save dataset into CSV file.
    """

    df = pd.DataFrame(dataset)

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nDataset saved successfully!")

    print(f"Location : {OUTPUT_PATH}")

    print(f"Total Rows : {len(df)}")
def main():

    dataset = create_dataset()

    save_dataset(dataset)


if __name__ == "__main__":
    main()