"""Functions for creating, transforming, and adding prefixes to strings."""

from typing import List


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word


def make_word_groups(vocab_words: List[str]) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    return_string: str = ""

    i = 0
    list_length = len(vocab_words)
    while i < list_length:
        if i == 0:
            return_string += vocab_words[i]
        else:
            return_string += vocab_words[0] + vocab_words[i]

        if i != list_length - 1:
            return_string += " :: "

        i = i + 1

    return return_string


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    suffix = "ness"
    trimmed_word = word[: -len(suffix)]
    if trimmed_word[len(trimmed_word) - 1 :] == "i":  # noqa: E203
        return trimmed_word[:-1] + "y"
    return trimmed_word


def adjective_to_verb(sentence: str, index: int):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    adjective = sentence.split(" ")[index]
    return adjective.replace(".", "") + "en"
