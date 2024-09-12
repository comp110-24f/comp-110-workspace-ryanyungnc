"""Input the # of guests and recieved how many ingredients and the cost of a tea party!"""

__author__: str = "730775886"


def main_planner(guests: int) -> None:
    """the entrypoint of my program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(
                tea_count=tea_bags(people=guests), treat_count=treats(people=guests)
            )  # tea_bags and treat_count are used to get inputs in for the function
        )  # code automatically indented when saving bc line was too long
    )


def tea_bags(people: int) -> int:
    """returns the amount of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """returns the amount of treats needed"""
    return int(
        tea_bags(people=people) * 1.5
    )  # need to use int as I am multiplying by an inproper number


def cost(tea_count: int, treat_count: int) -> float:
    """returns the cost of the tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# uses the main function after getting an input which needs to be converted to an int
