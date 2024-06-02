"""Arithmetic test project"""
from random import randint, choice

def get_choice(valid_choices):
    """Prompt user for a valid choice."""
    while True:
        try:
            choice = int(input("> "))
            if choice in valid_choices:
                return choice
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")

def check_answer(correct, user):
    """Check if user's answer is correct."""
    if user == correct:
        print("Right!")
        return True
    else:
        print("Wrong")
        return False

def get_answer():
    """Prompt user for an answer."""
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Wrong format! Try again.")

def simple_test(tasks):
    """Conduct a simple arithmetic test."""
    score = 0
    operations = ["+", "-", "*"]

    for i in range(tasks):
        num1 = randint(2, 9)
        num2 = randint(2, 9)
        op = choice(operations)

        print(num1, op, num2)

        user_answer = get_answer()

        if op == "+":
            correct_answer = num1 + num2
        elif op == "-":
            correct_answer = num1 - num2
        elif op == "*":
            correct_answer = num1 * num2

        score += check_answer(correct_answer, user_answer)

    return score

def hard_test(tasks):
    """Conduct a hard arithmetic test."""
    score = 0

    for i in range(tasks):
        number = randint(11, 29)
        print(number)

        user_answer = get_answer()
        correct_answer = number ** 2
        score += check_answer(correct_answer, user_answer)

    return score

levels = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}

print(f"Which level do you want? Enter a number:\n"
      f"1 - {levels.get(1)}\n"
      f"2 - {levels.get(2)}")

tasks_count = 5
score = 0
valid_choices = [1, 2]
level_choice = get_choice(valid_choices)

if level_choice == 1:
    score = simple_test(tasks_count)
elif level_choice == 2:
    score = hard_test(tasks_count)
else:
    print("Impossible")

print(f"Your mark is {score}. Would you like to save the result? Enter yes or no.")
save_result = input("> ")

if save_result.lower() == "yes":
    print("What is your name?")
    student_name = input("> ")
    result = f"{student_name}: {score}/{tasks_count} in level {level_choice} ({levels.get(level_choice)})."

    file_name = "results.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(result)

    print(f"The results are saved in \"{file_name}\".")

print("See you!")
