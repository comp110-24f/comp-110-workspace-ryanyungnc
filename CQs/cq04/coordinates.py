"""part of my challenge question 4"""

__author__ = "730775886"


def get_coords(xs: str, ys: str) -> None:
    count_x: int = 0  # will serve as the counter for x
    while count_x < len(xs):
        count_y: int = 0  # will serve as the counter for y and resets it to 0
        while count_y < len(ys):  # prints a unique comb and then moves to next one
            print("(" + xs[count_x] + "," + ys[count_y] + ")")
            count_y += 1  # to keep loop going on y
        count_x += 1  # to keep loop going on x
