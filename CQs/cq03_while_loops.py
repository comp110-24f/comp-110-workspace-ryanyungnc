"""Challenge question on while loops"""

__author__ = "730775886"


def num_instances(phrase: str, search_char: str) -> int:
    """this function uses a while loop to check how many times a character is within a phrase"""
    i: int = 0  # i will track how many while loops the function has gone through
    j: int = 0  # j will track how many times the char is in the phrase
    while i < len(phrase):  # loops as long as i is not greater than the str length
        if phrase[i] == search_char:
            j = (
                j + 1
            )  # if the char at the point i is the equal than add 1 to the overall count
        i = i + 1  # add one to the loop count
    return j  # returns the value of how many times the char is in the phrase
