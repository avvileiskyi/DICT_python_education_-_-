"""Arithmetic test project"""
from random import randint, choice


def get_level_choice(pos_values):
    """Prompts the user for a choice and validates it against a list of possible values

    Args:
        pos_values (list): list of possible values to choose from

    Returns:
        int: valid user choice selected from possible values
    """
    while True:
        try:
            level_choice = int(input("> "))
            if level_choice in pos_values:
                return level_choice
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def is_correct_answer(c_answer, u_answer):
    """Checks if the user's answer matches the correct answer

    Args:
        c_answer (int): correct answer
        u_answer (int): user's answer

    Returns:
        bool: True(1) if the answers match, False(0) otherwise
    """
    if u_answer == c_answer:
        print("Right!")
        return True
    else:
        print("Wrong")
        return False


def get_user_answer():
    """Prompts the user for an answer and handles incorrect formats

    Returns:
        int: user's input converted to an integer
    """
    while True:
        try:
            return int(input("> "))
        except ValueError:
            print("Wrong format! Try again.")


def start_simple_test(num_of_tasks):
    """Starts a simple arithmetic test with random numbers and basic operations

    Args:
        num_of_tasks (int): number of tasks in the test

    Returns:
        int: total mark obtained by the user in the test.
    """
    mark = 0
    operations = ["+", "-", "*"]

    for i in range(num_of_tasks):
        first_num = randint(2, 9)
        second_num = randint(2, 9)
        operation = choice(operations)

        print(first_num, operation, second_num)

        user_answer = get_user_answer()

        if operation == "+":
            correct_answer = first_num + second_num
            mark += is_correct_answer(correct_answer, user_answer)

        elif operation == "-":
            correct_answer = first_num - second_num
            mark += is_correct_answer(correct_answer, user_answer)

        elif operation == "*":
            correct_answer = first_num * second_num
            mark += is_correct_answer(correct_answer, user_answer)

    return mark


def start_hard_test(num_of_tasks):
    """Starts a harder arithmetic test with integral squares of random numbers

    Args:
        num_of_tasks (int): number of tasks in the test

    Returns:
        int: total mark obtained by the user in the test.
    """
    mark = 0

    for i in range(num_of_tasks):
        number = randint(11, 29)
        print(number)

        user_answer = get_user_answer()
        correct_answer = number**2
        mark += is_correct_answer(correct_answer, user_answer)

    return mark


levels = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}

print(f"Which level do you want? Enter a number:\n"
      f"1 - {levels.get(1)}\n"
      f"2 - {levels.get(2)}")

number_of_tasks = 5
student_mark = 0
possible_values = [1, 2]
user_level_choice = get_level_choice(possible_values)

if user_level_choice == 1:
    student_mark = start_simple_test(number_of_tasks)

elif user_level_choice == 2:
    student_mark = start_hard_test(number_of_tasks)

else:
    print("Impossible")

print(f"Your mark is {student_mark}. Would you like to save the result? Enter yes or no.")
save_result_choice = input("> ")

if save_result_choice.lower() == "yes":
    print("What is your name?")
    student_name = input("> ")
    student_result = (f"{student_name}: {student_mark}/{number_of_tasks} in level {user_level_choice} "
                      f"({levels.get(user_level_choice)}).")

    file_name = "results.txt"
    with open(file_name, "w", encoding="utf-8") as result_file:
        result_file.write(student_result)

    print(f"The results are saved in \"{file_name}\".")

print("See you!")