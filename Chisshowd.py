def welcome():
    """Displays a welcome message for the Christmas Show."""
    print("Welcome to the Christmas Show!")

def system():
    """Checks for a guest and starts the Christmas show."""

    guest = input("Guest detected? Yes(Y/y) or No(N/n)\n")

    if guest == "Y" or guest == "y":
        santadance()

    if guest == "N" or guest == "n":
        print("Waiting for guest")


def santadance():
    """Reads the show file and controls Santa's dance steps."""

    print("Santa makes a grand enterance on his sleigh!")

    with open('show.txt', 'r') as file:
        guest = file.readline().strip()
        steps = int(file.readline().strip())
        end = int(file.readline().strip())

    while steps < 6:
        dance = int(input("Santa can dance up to 6 steps \nEnter steps: "))
        steps = steps + dance

        print("Santa dances", steps, "steps")
        print("Elves follow Santa")
        print("Moves left:", 6 - steps)

    # if steps <= 0:
    #     print("Santa is not dancing")

    if steps > 6:
        print("Too many steps!")
        print("Santa falls on the elves!:o")
        system()

    if steps == 6:
        print("Santa used all his moves!")
        endshow()


def endshow():
    """Ends the Christmas show and displays a Christmas tree."""

    steps = 6

    print("Show has ended! ")
    print("     *")
    print("    ***")
    print("   *****")
    print("  *******")
    print("     |")

    # print("Waiting for next guest")
    # return system


def goodbye():
    """Displays a goodbye message after the Christmas Show."""
    print("Thank you for watching the Christmas Show!")


if __name__ == "__main__":
    system()
