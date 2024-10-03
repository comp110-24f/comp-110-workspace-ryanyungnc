"""EX03 - Wordle - Creating a game in python!"""

__author__ = "730775886"


def input_guess(secret_word_len: int) -> str:
    """prompts the user to enter a guess of a certain length and returns it when done"""
    guessed_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guessed_word) != secret_word_len:  # repeats until input = desired len
        guessed_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guessed_word  # returns what they inputted within len specification


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks whether a char is present at any point in a word"""
    assert len(char_guess) == 1  # returns error if char entered is not len 1
    loop_num: int = 0  # int to keep track of times looped
    while loop_num < len(secret_word):  # looping through every char in word
        if secret_word[loop_num] == char_guess:
            return True  # goes through each char & if true return that, ending fn
        loop_num += 1  # adds 1 to the loop
    return False  # if gone through whole word then return false


def emojified(users_guess: str, secret_word: str) -> str:
    """compares two strings of equal length and returns a str made of emojis"""
    assert len(users_guess) == len(secret_word)  # returns error if strs arent equal len
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"  # 3 named constants representing emojis
    loop_num: int = 0  # int to keep track of times looped
    emoji_str: str = ""  # creates a blank str that we will add emojis to & return
    while loop_num < len(secret_word):  # loops the length of the str
        if users_guess[loop_num] == secret_word[loop_num]:
            emoji_str += GREEN_BOX  # if chars match at loop num then +greenbox to str
        elif contains_char(secret_word=secret_word, char_guess=users_guess[loop_num]):
            emoji_str += YELLOW_BOX  # if char is somewhere in word then +yellowbox
        else:
            emoji_str += WHITE_BOX  # if not anywhere then +whitebox to str
        loop_num += 1  # move onto next letter in loop
    return emoji_str  # returns emoji str with added emojis from loop


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn_num: int = 0  # int to keep track of num of turns
    while turn_num < 6:  # loops 6 times, giving 6 turns
        print(f"=== Turn {turn_num + 1}/6 ===")  # prints fancy turn number
        checked_guess: str = emojified(
            users_guess=input_guess(secret_word_len=len(secret)), secret_word=secret
        )  # runs emojified and secret_word_len fns and stores emoji str in a variable
        print(checked_guess)  # prints the emoji str
        if checked_guess == ("\U0001F7E9" * len(secret)):  # checks is str is all green
            print(f"You won in {turn_num + 1}/6 turns!")  # displays turns won in
            return None  # exits function early bc user won
        turn_num += 1  # progresses to the next turn
    print("X/6 - Sorry, try again tomorrow!")  # displays losing msg
    return None  # exits function


if __name__ == "__main__":
    main(secret="codes")
