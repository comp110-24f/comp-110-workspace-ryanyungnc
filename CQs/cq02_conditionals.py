"""Challenge question on conditionals"""

__author__ = "730775886"


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:  # checks if x is equal to the secret num
        print("You got it!")
    elif x < secret:  # if it is less than secret num
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # if it is the final condition
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
