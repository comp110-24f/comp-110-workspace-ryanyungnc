"""Writing functions for CQ07!"""

__author__ = "730775886"


def find_and_remove_max(input: list[int]) -> int:
    """finds, returns, and removes the largest num in a list"""
    if len(input) == 0:
        return -1  # if empty list end func and return -1
    max: int = input[0]
    for value in input:
        if max < value:  # loops through every val of list
            max = value  # and if num at point is > max reassigns it to max
    i: int = 0  # counter variable
    while i < len(input):
        if max == input[i]:  # if equal to max remove it
            input.pop(i)
        else:
            i += 1  # only needs to progress if an item isnt removed
    return max
