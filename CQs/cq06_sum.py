"""Summing the elements of a list using different loops"""

__author__ = "730775886"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats using a while loop"""
    i: int = 0  # counter variable
    sum_val: float = 0.0  # will keep track of the total sum as it loops
    while i < len(vals):  # loops through every part of vals list
        sum_val += vals[i]  # adds part of val list to total
        i += 1  # progresses the loop
    return sum_val  # returns sum of vals


def f_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats using a for ... in ... loop"""
    sum_val: float = 0.0  # will keep track of the total sum as it loops
    for value in vals:  # loops through each part of vals list
        sum_val += value  # adds value of each part to total
    return sum_val  # returns total sum of vals


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of a list of floats using a for ... in range() loop"""
    sum_val: float = 0.0  # will keep track of the total sum as it loops
    for value in range(0, len(vals), 1):  # starts at item 0, iterates through vals
        sum_val += vals[value]  # same as before
    return sum_val  # returns total sum of vals
