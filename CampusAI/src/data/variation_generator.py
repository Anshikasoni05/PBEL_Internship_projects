import random
from nltk.corpus import wordnet

from src.utils.synonyms import SYNONYMS
QUESTION_PREFIXES = [
    "",
    "Can you tell me ",
    "Could you tell me ",
    "Please tell me ",
    "I want to know ",
    "Can you explain ",
    "Kindly tell me ",
    "May I know "
]
def get_wordnet_synonyms(word):
    """
    Get synonyms from WordNet.
    """

    synonyms = set()

    for syn in wordnet.synsets(word):

        for lemma in syn.lemmas():

            synonym = lemma.name().replace("_", " ")

            if synonym.lower() != word.lower():
                synonyms.add(synonym.lower())

    return list(synonyms)
def get_all_synonyms(word):

    synonyms = set()

    if word in SYNONYMS:
        synonyms.update(SYNONYMS[word])

    synonyms.update(get_wordnet_synonyms(word))

    return list(synonyms)
if __name__ == "__main__":

    print(get_all_synonyms("scholarship"))