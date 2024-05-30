"""Rock Paper Scissors module"""
from random import choice


def get_user_rating(username):
    """Gets the user's rating from the 'rating' file if it's possible

    Args:
        username (str): user's name

    Returns:
        int: user's rating points
    """
    with open("rating", "r", encoding="utf-8") as file:
        for line in file:
            name, points = line.split()
            if username == name:
                return int(points)
    return 0


def start_game(user_option, rules):
    """Starts a round of the Rock Paper Scissors game

    Args:
        user_option (str): user's choice
        rules (dict): dictionary with game rules

    Returns:
        int: points earned in the round
    """
    computer_option = choice(list(rules.keys()))

    if computer_option in rules[user_option]:
        print(f"Well done. The computer chose {computer_option} and failed")
        return 100
    elif user_option == computer_option:
        print(f"There is a draw ({user_option})")
        return 50
    else:
        print(f"Sorry, but the computer chose {computer_option}")
        return 0


def print_rules(rules):
    """Prints the game rules

    Args:
        rules (dict): dictionary with game rules
    """
    for option in rules:
        print(f"{option} can beat: {', '.join(rules[option])}")


def get_user_rules(options):
    """Gets user-defined rules from a list of options

    Args:
        options (list): list of user-defined options

    Returns:
        dict: user-defined game rules
    """
    rules = {}

    for i in range(len(options)):
        rules[options[i]] = [options[i] for i in range(i-len(options)//2, i)]

    return rules


def start_menu():
    """Start the main menu of the Rock Paper Scissors game"""

    name = input("Enter your name: > ")
    print(f"Hello, {name}")

    options = input("Enter the options in format \"rock,paper,scissors\": > ")
    print("Okay, let's start")

    user_rating = get_user_rating(name)
    default_rules = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
    rules = default_rules if options == '' else get_user_rules(options.split(","))

    while True:
        user_choice = input("> ")
        if user_choice == "!exit":
            print("Bye!")
            break

        elif user_choice == "!rules":
            print_rules(rules)

        elif user_choice == "!rating":
            print(f"Your rating is {user_rating}!")

        elif user_choice in rules.keys():
            user_rating += start_game(user_choice, rules)

        else:
            print("Incorrect input.")


if __name__ == "__main__":
    start_menu()

