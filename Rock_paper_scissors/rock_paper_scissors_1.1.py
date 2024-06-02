"""Rock Paper Scissors module"""
from random import choice

def get_rating(username):
    """Get user's rating from file."""
    with open("rating.txt", "r") as file:
        for line in file:
            name, points = line.split()
            if username == name:
                return int(points)
    return 0

def play_round(user_choice, game_rules):
    """Play a round of Rock Paper Scissors."""
    computer_choice = choice(list(game_rules.keys()))

    if computer_choice in game_rules[user_choice]:
        print(f"Well done. The computer chose {computer_choice} and failed")
        return 100
    elif user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        return 50
    else:
        print(f"Sorry, but the computer chose {computer_choice}")
        return 0

def display_rules(game_rules):
    """Display the game rules."""
    for option in game_rules:
        print(f"{option} can beat: {', '.join(game_rules[option])}")

def generate_rules(options):
    """Generate user-defined rules."""
    rules = {}
    for i in range(len(options)):
        rules[options[i]] = [options[j % len(options)] for j in range(i + 1, i + len(options) // 2 + 1)]
    return rules

def start_menu():
    """Start the main menu."""
    name = input("Enter your name: > ")
    print(f"Hello, {name}")

    options = input("Enter the options in format \"rock,paper,scissors\": > ")
    print("Okay, let's start")

    user_rating = get_rating(name)
    default_rules = {"rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"]}
    game_rules = default_rules if options == '' else generate_rules(options.split(","))

    while True:
        user_input = input("> ")
        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rules":
            display_rules(game_rules)
        elif user_input == "!rating":
            print(f"Your rating is {user_rating}!")
        elif user_input in game_rules.keys():
            user_rating += play_round(user_input, game_rules)
        else:
            print("Incorrect input.")

if __name__ == "__main__":
    start_menu()
