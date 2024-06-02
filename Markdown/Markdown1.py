"""Simple markdown editor module"""

def plain_text():
    """Get plain text from user."""
    text = input("Text: > ")
    return text

def bold_text():
    """Get bold text from user."""
    text = input("Text: > ")
    return f"**{text}**"

def italic_text():
    """Get italic text from user."""
    text = input("Text: > ")
    return f"*{text}*"

def inline_code_text():
    """Get inline code text from user."""
    text = input("Text: > ")
    return f"`{text}`"

def header_level():
    """Get header level from user."""
    levels = [1, 2, 3, 4, 5, 6]
    while True:
        try:
            level = int(input("Level: > "))
            if level in levels:
                return level
            print("The level should be within the range of 1 to 6")
        except ValueError:
            print("The value must be numeric")

def header_text():
    """Get header text from user."""
    level = header_level()
    text = input("Text: > ")
    return f"{'#' * level} {text}"

def new_line():
    """Add new line."""
    return "\n"

def link_text():
    """Get link text from user."""
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

def row_count():
    """Get number of rows for list."""
    while True:
        try:
            count = int(input("Number of rows: > "))
            if count > 0:
                return count
            print("The number of rows should be greater than zero")
        except ValueError:
            print("The value must be numeric")

def create_list(is_ordered):
    """Get list from user."""
    result = ""
    count = row_count()
    for i in range(count):
        item = input(f"Row #{i+1}: > ")
        result += "\n" + (f"{i+1}. {item}" if is_ordered else f"* {item}")
    result += "\n"
    return result

formatters = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line"]
commands = ["!help", "!done"]
output = ""

while True:
    formatter = input("Choose a formatter: > ")
    if formatter == "plain":
        output += plain_text()
    elif formatter == "bold":
        output += bold_text()
    elif formatter == "italic":
        output += italic_text()
    elif formatter == "inline-code":
        output += inline_code_text()
    elif formatter == "link":
        output += link_text()
    elif formatter == "header":
        output += header_text()
    elif formatter == "unordered-list":
        output += create_list(is_ordered=False)
    elif formatter == "ordered-list":
        output += create_list(is_ordered=True)
    elif formatter == "new-line":
        output += new_line()
    elif formatter == "!help":
        print("Available formatters: ", *formatters)
        print("Special commands: ", *commands)
        continue
    elif formatter == "!done":
        with open("output.md", "w", encoding="utf-8") as result_file:
            result_file.write(output)
        break
    else:
        print("Unknown formatting type or command")
        continue
    print(output)
