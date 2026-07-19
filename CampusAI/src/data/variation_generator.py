import random
from src.utils.synonyms import SYNONYMS

# Question Templates
TEMPLATES = [
    "{}",
    "Can you tell me {}?",
    "Please tell me {}",
    "I want to know {}",
    "Could you explain {}?",
    "Give me information about {}",
    "Tell me about {}",
    "What is {}?",
    "Can you help me with {}?",
    "I need information regarding {}"
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
    """
    Generate all possible variations.
    """

    dataset = set()

    # Original
    dataset.add(sentence)

    # Synonym Replacement
    synonym_versions = synonym_replacement(sentence)

    for item in synonym_versions:

        dataset.add(item)

    # Template Variations
    for item in synonym_versions:

        template_versions = template_variations(item)

        for temp in template_versions:

            dataset.add(temp)

    return list(dataset)