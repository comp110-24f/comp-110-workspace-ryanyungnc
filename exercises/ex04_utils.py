"""EX04 - Utils - Reverse Engineering Functions"""

__author__ = "730775886"


def all(nums: list[int], check: int) -> bool:
    """If all nums equal check return true, otherwise return false"""
    if len(nums) == 0:
        return False  # if no values in list, check cant be in list
    for num in nums:  # rotates through all values in the nums list
        if num != check:  # checks if num isnt the same
            return False  # ends the loop & returns false
    return True  # all nums passed so returns true


def max(nums: list[int]) -> int:
    """Given a list of ints, returns the largest in the list"""
    if len(nums) == 0:  # returns error if inputted list is empty
        raise ValueError("max() arg is an empty List")
    top: int = nums[1]  # created variable to track the biggest num; initially 1st value
    for num in nums:  # rotates through all values in the nums list
        if num > top:
            top = num  # if num is bigger than current top replace it
    return top  # return biggest num in list


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if 2 lists are deeply equal in value"""
    if len(list1) != len(list2):
        return False  # if lists are not equal length they are not equal (remove error)
    for num in range(0, len(list1), 1):  # used range so i can get num in loop not value
        if list1[num] != list2[num]:
            return False  # if nums not equal at point return false
    return True  # if all checks passed, return true


def extend(list1: list[int], list2: list[int]) -> None:
    """Adds list2 values to the end of list1"""
    for num in list2:  # rotates through every value of list2
        list1.append(num)  # adds every value to the end of list1
    return None  # returns none
