import re


def clean_text(text):
    """
    Clean user input before prediction.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


if __name__ == "__main__":

    sample = "  Hello!!!   How Can I Take Admission??? "

    print("Original :", sample)

    print("Processed:", clean_text(sample))