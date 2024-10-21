"""Testing different functions."""


def get_first(input: list[str]) -> str:
    """returns the first element in the list."""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Pop the first element off of input list."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """returns the first element and removes it from the list"""
    first: str = input[0]
    input.pop(0)
    return first
