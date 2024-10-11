"""Mutating functions."""

__author__ = "730775886"


def manual_append(list: list[int], add: int) -> None:
    """adds add var to end of list"""
    list.append(add)  # adds the var to the end of list
    return None  # end function


def double(list: list[int]) -> None:
    """doubles every item in the inputed list"""
    i: int = 0  # initialize the counting variable
    while i < len(list):  # cycles through every item in the list
        list[i] = list[i] * 2  # replaces the list item w itself * 2
        i += 1  # progress the loop
    return None  # end function


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list=list_2)
print(list_1)
print(list_2)
