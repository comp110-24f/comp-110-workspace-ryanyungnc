"""Testing functions in find_max.py!"""

__author__ = "730775886"

from find_max import find_and_remove_max


def test_find_and_remove_max_value() -> None:  # tests for expected value returned of 9
    assert find_and_remove_max(input=[6, 5, 9, 7, 2, 9, 8, 5, 8, 1]) == 9


def test_find_and_remove_max_mutation() -> None:  # tests for the expected list
    a: list[int] = [6, 5, 9, 7, 2, 9, 8, 5, 8, 1]
    find_and_remove_max(input=a)
    assert a == [6, 5, 7, 2, 8, 5, 8, 1]  # checks if equal to list that I would expect


def test_find_and_remove_max_edge_case() -> None:
    assert find_and_remove_max(input=[]) == -1  # checks for an edgecase of empty list
