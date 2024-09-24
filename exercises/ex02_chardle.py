"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730775886"


def input_word() -> str:
    word: str = input(
        "Enter a 5-character word: "
    )  # asks and stores a 5 character word
    if len(word) == 5:
        return word  # if the length of the word is 5 then return the word
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # if error then exit the function after giving error msg


def input_letter() -> str:
    letter: str = input(
        "Enter a single character: "
    )  # asks and stores a single character
    if len(letter) != 1:  # checks if it is not a single character and gives error msg
        print("Error: Character must be a single character.")
        exit()  # if error then exit the function after giving error msg
    return letter  # returns the letter no matter error


def contains_char(word: str, letter: str) -> None:
    loop_num: int = 0  # will keep track of what num letter loop is on
    count: int = 0  # will keep track of times letter shows up in word
    print("Searching for " + letter + " in " + word)  # notifies the user
    while loop_num < 5:  # loops 5 times
        if word[loop_num] == letter:  # checks if each letter is equal to letter input
            print(letter + " found at index " + str(loop_num + 1))  # if so, prints it
            count = count + 1  # adds 1 to the count if the letter appears in word
        loop_num = loop_num + 1  # progresses the loop
    if count == 0:  # checks if there is no letter match and reports it
        print("No instances of " + letter + " found in " + word)
    else:  # otherwise report how many letters match
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # main which calls the contains char function w inputs
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":  # calls main when hit run program
    main()
