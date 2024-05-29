"""Simplified markdown editor module"""


def add_plain_text():
    """Gets some text from the user and transforms it to plain text

    Returns:
        str: plain text
    """
    user_text = input("Text: > ")
    return user_text


def add_bold_text():
    """Gets some text from the user and transforms it to bold text

    Returns:
        str: bold text
    """
    user_text = input("Text: > ")
    return f"**{user_text}**"


def add_italic_text():
    """Gets some text from the user and transforms it to italic text

    Returns:
        str: italic text
    """
    user_text = input("Text: > ")
    return f"*{user_text}*"


def add_inline_code():
    """Gets some text from the user and transforms it to inline code text

    Returns:
        str: inline code
    """
    user_text = input("Text: > ")
    return f"`{user_text}`"


def get_level():
    """Gets the header level from the user

    Returns:
        int: level from 1 to 6
    """
    possible_values = [1, 2, 3, 4, 5, 6]

    while True:
        try:
            user_choice = int(input("Level: > "))
            if user_choice in possible_values:
                return user_choice
            print("The level should be within the range of 1 to 6")

        except ValueError:
            print("The value must be numeric")


def add_header():
    """Gets the level and some text from the user and transforms it to header text

    Returns:
        str: header text
    """
    level = get_level()
    user_text = input("Text: > ")

    while True:
        if level == 1:
            return f"# {user_text}"

        elif level == 2:
            return f"## {user_text}"

        elif level == 3:
            return f"### {user_text}"

        elif level == 4:
            return f"#### {user_text}"

        elif level == 5:
            return f"##### {user_text}"

        elif level == 6:
            return f"###### {user_text}"


def add_new_line():
    """Creates new line

    Returns:
        str: new line symbol
    """
    return "\n"


def add_link():
    """Gets label and URL from the user and transforms it to link with label

    Returns:
        str: link with label
    """
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"


def get_rows_count():
    """Get the number of rows for a list

    Returns:
        int: number of rows
    """
    while True:
        try:
            rows_count = int(input("Number of rows: > "))
            if rows_count > 0:
                return rows_count
            print("The number of rows should be greater than zero")

        except ValueError:
            print("The value must be numeric")


def add_list(is_ordered):
    """Gets number of rows and some text from the user and transforms it to ordered/unordered list

    Args:
        is_ordered (boolean): True for ordered list, False for unordered list

    Returns:
        str: ordered/unordered list
    """
    result = ""
    rows_count = get_rows_count()

    for i in range(rows_count):
        element = input(f"Row #{i+1}: > ")

        result += f"{i+1}. {element}" if is_ordered else f"* {element}"
        result += "" if rows_count == i + 1 else "\n"

    return result

available_formatters = ["plain", "bold", "italic", "inline-code", "link",
                        "header", "unordered-list", "ordered-list", "new-line"]
special_commands = ["!help", "!done"]
result = ""

while True:
    user_formatter = input("Choose a formatter: > ")
    if user_formatter == "plain":
        result += add_plain_text()

    elif user_formatter == "bold":
        result += add_bold_text()

    elif user_formatter == "italic":
        result += add_italic_text()

    elif user_formatter == "inline-code":
        result += add_inline_code()

    elif user_formatter == "link":
        result += add_link()

    elif user_formatter == "header":
        result += add_header()

    elif user_formatter == "unordered-list":
        result += add_list(is_ordered=False)

    elif user_formatter == "ordered-list":
        result += add_list(is_ordered=True)

    elif user_formatter == "new-line":
        result += add_new_line()

    elif user_formatter == "!help":
        print("Available formatters: ", *available_formatters)
        print("Special commands: ", *special_commands)
        continue

    elif user_formatter == "!done":
        with open("output.md", "w", encoding="utf-8") as result_file:
            result_file.write(result)
        break

    else:
        print("Unknown formatting type or command")
        continue

    print(result)