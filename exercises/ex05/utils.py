"""EX05 - Learning more about testing and using lists!"""

__author__ = "730775886"


def only_evens(input: list[int]) -> list[int]:
    """returns given list with only even nums"""
    newlist: list[int] = []  # create a blank new list
    for item in input:  # for each item in the list
        if item % 2 == 0:  # if item is even (mod equaling 0 means even for /2)
            newlist.append(item)  # add item to new list of only evens
    return newlist  # returns the created list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Creates a new list within the subset parameters inputted"""
    newlist: list[int] = []  # create a blank new list
    for item in range(0, len(input), 1):  # loops through each item in list
        if item >= start and item < end:  # if item is within parameters
            newlist.append(input[item])  # add to new list
    return newlist  # returns new list within inputted parameters


def add_at_index(input: list[int], add: int, place: int) -> None:
    """adds int to a given place in the input list"""
    if place > len(input) or place < 0:  # checks for edge case of not in list
        raise IndexError("Index is out of bounds for the input list")  # gives errors
    input.append(0)  # adds placeholder num to end of list
    for num in range(len(input) - 1, place, -1):
        input[num] = input[num - 1]  # moving all nums up 1 value, from back to front
    input[place] = add  # sets num at place to value inputted
    return None
