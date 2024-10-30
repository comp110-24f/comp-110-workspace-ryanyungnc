"""Testing functions in utils.py - part of EX05"""

__author__ = "730775886"

from utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_value() -> None:
    """use case 1 - tests for the expected value returned when only_evens used"""
    assert only_evens([1, 2, 3, 6, 5, 9, 4, 6]) == ([2, 6, 4, 6])


def test_only_evens_modify() -> None:
    """use case 2 - tests that the original list is not modified when only_evens used"""
    x: list[int] = [1, 2, 3, 6, 5, 9, 4, 6]
    only_evens(x)
    assert x == [1, 2, 3, 6, 5, 9, 4, 6]  # original numbers before function was used


def test_only_even_edge_case() -> None:
    """edge case - returns an empty list when an empty list is inputted"""
    assert only_evens([]) == []  # should give back an empty list as no evens in empty


def test_sub_value() -> None:
    """use case 1 - tests for the expected value returned when sub used"""
    assert sub([1, 2, 3, 6, 5, 9, 4, 6], 3, 7) == [6, 5, 9, 4]


def test_sub_modify() -> None:
    """use case 2 - tests that the original list isnt modified when sub used"""
    x: list[int] = [1, 2, 3, 6, 5, 9, 4, 6]
    sub(x, 2, 5)  # using function before checking
    assert x == [1, 2, 3, 6, 5, 9, 4, 6]  # x should be same as function makes new lists


def test_sub_edge_case() -> None:
    """edge case - test that when an empty list is inputted nothing is outputted"""
    assert sub([], 0, 3) == []


def test_add_at_index_value() -> None:
    """use case 1 - tests that expected value of None is returned from add_at_index"""
    assert add_at_index([1, 2, 3, 5, 9, 4, 6], 6, 4) is None


def test_add_at_index_modify() -> None:
    """use case 2 - tests for expected modification of list after add_at_index"""
    x: list[int] = [1, 2, 3, 5, 9, 4, 6]
    add_at_index(x, 6, 3)  # using function before checking
    assert x == [1, 2, 3, 6, 5, 9, 4, 6]  # x should change bc function modifies lists


def test_add_at_index_edge_case() -> None:
    """edge case - test that add_at_index raises an IndexError for invalid index"""
    with pytest.raises(
        IndexError
    ):  # different syntax to check as we are checking for error
        add_at_index([1, 2, 3, 6], 5, 9)
