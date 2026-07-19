import random
from src.utils.synonyms import SYNONYMS

# Question Templates
TEMPLATES = [

    "{}",

    "Can you tell me {}?",
    "Please tell me {}.",
    "I want to know {}.",
    "Could you explain {}?",
    "Give me information about {}.",
    "Tell me about {}.",
    "What is {}?",
    "Can you help me with {}?",
    "I need information regarding {}.",

    "May I know {}?",
    "Could you please tell me {}?",
    "Would you explain {}?",
    "Please provide details about {}.",
    "Can you provide information about {}?",
    "I would like to know {}.",
    "Can you guide me regarding {}?",
    "Please explain {}.",
    "I have a question about {}.",
    "Can you answer my question about {}?",
    "Tell me more about {}.",
    "Give me complete details about {}.",
    "Can you clarify {}?",
    "I need help regarding {}.",
    "Please help me understand {}.",
    "How to {}?",
    "How do I {}?",
    "How can I {}?",
    "Where can I {}?",
    "Guide me to {}",
    "What is the process for {}?",
    "Can you explain how to {}?",
    "I want to {}",
    "Steps to {}",
    "Procedure for {}"
]


def synonym_replacement(sentence):
    """
    Replace words with synonyms.
    """
    variations = set()

    variations.add(sentence)

    words = sentence.lower().split()

    for i, word in enumerate(words):

        clean_word = word.strip("?,.!")

        if clean_word in SYNONYMS:

            for synonym in SYNONYMS[clean_word]:

                new_words = words.copy()

                new_words[i] = synonym

                variations.add(" ".join(new_words).capitalize())

    return list(variations)


def template_variations(sentence):
    """
    Generate template-based variations.
    """

    variations = []

    sentence = sentence.lower()

    for template in TEMPLATES:

        variations.append(template.format(sentence).capitalize())

    return variations


def generate_variations(sentence):

    dataset = set()

    synonym_versions = synonym_replacement(sentence)

    for item in synonym_versions:

        dataset.add(item)

        for template in template_variations(item):

            dataset.add(template)

            dataset.add(template.lower())

            dataset.add(template.upper())

            dataset.add(template.capitalize())

    return list(dataset)