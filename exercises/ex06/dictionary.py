"""EX06 - Dictionary Practice!"""

__author__ = "730775886"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Takes a given dict and returns the inverse"""
    i: int = 0  # will store what value check1 is on
    for check1 in input:
        j: int = 0  # will store what value check2 is on
        for check2 in input:  # if values are the same and in same spot then ignore
            if input[check1] == input[check2] and i != j:  # if diff spot then error
                raise KeyError("Cannot have duplicate values!")
            j += 1  # continue loop
        i += 1  # continue loop
    inverted_dict: dict[str, str] = {}
    for key in input:  # assign values inverted to a 2nd list
        inverted_dict[input[key]] = key
    return inverted_dict  # return that new list


def favorite_color(input: dict[str, str]) -> str:
    """Takes a list of names and colors and returns the most popular color"""
    preferences: dict[str, int] = {}  # empty list storing # of times each color appears
    for name in input:
        if input[name] in preferences:  # if existing already add 1 to value
            preferences[input[name]] += 1  # in learned from step 3 instruction
        else:  # if not existing in preferences list then create new one
            preferences[input[name]] = 1
    preferences["default"] = -1  # initializes a default value
    favorite: str = "default"  # cannot know which one to pick in list so use default
    for name in preferences:  # if next one is more pop then previous then make new fav
        if preferences[name] > preferences[favorite]:
            favorite = name  # new favorite
    if favorite == "default":
        return ""  # return nothing if nothing is inputted
    else:
        return favorite  # return favorite color


def count(input: list[str]) -> dict[str, int]:
    """given a list will compile a dict with how many times each value shows up"""
    value_count: dict[str, int] = {}  # empty list to store values in
    for item in input:  # loop through each item
        if item in value_count:  # check if already initialized in dict
            value_count[item] += 1  # add to old value
        else:
            value_count[item] = 1  # initialize new value
    return value_count  # return new dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """given a list will categorize them into words and return that"""
    letter_count: dict[str, list[str]] = {}  # empty list to store vals in
    for item in input:  # loop through each item
        if item[0] in letter_count:  # check if letter alr intialized in dict
            letter_count[item[0]].append(item)
        else:  # if not intialize it
            letter_count[item[0]] = [item]
    return letter_count  # return new list


def update_attendance(input: dict[str, list[str]], date: str, name: str) -> None:
    """given a dict and 2 str will mutate the string to mark attendances"""
    if date in input:
        input[date].append(name)
    else:
        input[date] = [name]
    return None
