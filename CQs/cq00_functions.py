"""My first challenge question on functions"""

__author__ = "730775886"


def mimic(message: str) -> str:
    """Takes a text input and returns it right back"""
    return message


def main() -> None:
    """The main sequence of my program"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
