"""part of my challenge question 4"""

__author__ = "730775886"


def concat(word1: str, word2: str) -> str:
    """returns the concatenation of 2 words"""
    return word1 + word2  # returns the 2 words inputed added together


if __name__ == "__main__":
    word1 = "happy"
    word2 = "tuesday"
    print(concat(word1, word2))  # prints the result of running concat w word1 and word2
