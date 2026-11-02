import re
from collections.abc import Collection

import numpy as np


def create_unique_word_dict(text: list[str]) -> dict[str, int]:
    """
    A method that creates a dictionary where the keys are unique words
    and key values are indices
    """
    # Getting all the unique words from our text and sorting them alphabetically
    words = list(set(text))
    words.sort()

    # Creating the dictionary for the unique words
    unique_word_dict = {}
    for i, word in enumerate(words):
        unique_word_dict.update({word: i})

    return unique_word_dict


def text_preprocessing(
    text: str,
    punctuations: str = r"""!()-[]{};:'"\,<>./?@#$%^&*_“~""",
    stop_words: Collection[str] = ("and", "a", "is", "the", "in", "be", "will"),
) -> list[str]:
    """
    A method to preproces text
    """
    for x in text.lower():
        if x in punctuations:
            text = text.replace(x, "")

    # Removing words that have numbers in them
    text = re.sub(r"\w*\d\w*", "", text)

    # Removing digits
    text = re.sub(r"[0-9]+", "", text)

    # Cleaning the whitespaces
    text = re.sub(r"\s+", " ", text).strip()

    # Setting every word to lower
    text = text.lower()

    # Converting all our text to a list
    tokens = text.split(" ")

    # Droping empty strings
    tokens = [x for x in tokens if x != ""]

    # Droping stop words
    tokens = [x for x in tokens if x not in stop_words]

    return tokens


# Functions to find the most similar word
def euclidean(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    A function to calculate the euclidean distance between two vectors
    """
    return float(np.sqrt(np.sum((vec1 - vec2) ** 2)))


def find_similar(
    word: str, embedding_dict: dict[str, np.ndarray], top_n: int = 10
) -> list[tuple[str, float]]:
    """
    A method to find the most similar word based on the learnt embeddings
    """
    dist_dict = {}
    word_vector = embedding_dict.get(word)
    if word_vector is None or len(word_vector) == 0:
        return []

    for key, value in embedding_dict.items():
        if key != word:
            dist = euclidean(word_vector, value)
            dist_dict.update({key: dist})

    return sorted(dist_dict.items(), key=lambda x: x[1])[0:top_n]
