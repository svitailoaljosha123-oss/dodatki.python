import sys

from teacher_functions import (
    FACULTY,
    load_teachers,
    add_teacher,
    show_teachers,
    edit_teacher,
    delete_teacher,
    rate_teacher,
    show_top,
)

MENU = [
    ("add", "Add teacher", add_teacher),
    ("show", "Show teachers", show_teachers),
    ("edit", "Edit teacher", edit_teacher),
    ("delete", "Delete teacher", delete_teacher),
    ("rate", "Rate teacher", rate_teacher),
    ("top", "Top teachers", show_top),
]

EXIT_NAME = "exit"
EXIT_NUMBER = str(len(MENU) + 1)  


def print_menu():
    print(f"\nTaskHub CLI - {FACULTY}")
    for number, (name, description, _) in enumerate(MENU, start=1):
        print(f"{number} - {description} ({name})")
    print(f"{EXIT_NUMBER} - Exit ({EXIT_NAME})")


def find_command(choice):
   
    for number, (name, _, function) in enumerate(MENU, start=1):
        if choice == str(number) or choice == name:
            return function
    return None


def main():
    teachers = load_teachers()

    one_shot = False
    start_command = None

    if len(sys.argv) > 1:
        start_command = sys.argv[1].lower()
        one_shot = True

    while True:
        if start_command is not None:
            choice = start_command
            start_command = None
        else:
            print_menu()
            choice = input("Choose command: ").strip().lower()

        if choice in (EXIT_NAME, EXIT_NUMBER):
            print("Goodbye!")
            break

        function = find_command(choice)
        if function is None:
            print("Unknown command!")
        else:
            function(teachers)

        if one_shot:
            break


if __name__ == "__main__":
    main()
