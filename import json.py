import json
import os
import sys

FILE = "teachers.json"
FACULTY = "Математичний факультет"

COMMANDS = {
    "add": "1",
    "show": "2",
    "edit": "3",
    "delete": "4",
    "rate": "5",
    "exit": "6",
}


def load_teachers():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_teachers(teachers):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(teachers, file, ensure_ascii=False, indent=4)


def average(teacher):
    if len(teacher["grades"]) == 0:
        return None
    return sum(teacher["grades"]) / len(teacher["grades"])


def show_names(teachers):
    for i in range(len(teachers)):
        print(f"{i + 1}. {teachers[i]['name']}")


def add_teacher(teachers):
    name = input("Enter teacher full name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    teacher = {
        "name": name,
        "faculty": FACULTY,
        "grades": []
    }

    teachers.append(teacher)
    save_teachers(teachers)
    print("Teacher added!")


def show_teachers(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    print(f"\nTeachers ({FACULTY}):")

    for i in range(len(teachers)):
        avg = average(teachers[i])

        if avg is None:
            rating = "no grades"
        else:
            rating = f"{avg:.2f} / 5 ({len(teachers[i]['grades'])} grades)"

        print(f"{i + 1}. {teachers[i]['name']} - {rating}")


def edit_teacher(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    show_names(teachers)
    number = input("Enter teacher number: ")

    if not number.isdigit():
        print("Enter a number!")
        return

    number = int(number)
    if not (1 <= number <= len(teachers)):
        print("Wrong teacher number!")
        return

    new_name = input("Enter new name: ").strip()

    if new_name == "":
        print("Name cannot be empty!")
        return

    teachers[number - 1]["name"] = new_name
    save_teachers(teachers)
    print("Teacher changed!")


def delete_teacher(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    show_names(teachers)
    number = input("Enter teacher number: ")

    if not number.isdigit():
        print("Enter a number!")
        return

    number = int(number)
    if not (1 <= number <= len(teachers)):
        print("Wrong teacher number!")
        return

    teachers.pop(number - 1)
    save_teachers(teachers)
    print("Teacher deleted!")


def rate_teacher(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    show_names(teachers)
    number = input("Enter teacher number: ")

    if not number.isdigit():
        print("Enter a number!")
        return

    number = int(number)
    if not (1 <= number <= len(teachers)):
        print("Wrong teacher number!")
        return

    grade = input("Enter grade (1-5): ")

    if not (grade.isdigit() and 1 <= int(grade) <= 5):
        print("Grade must be a number from 1 to 5!")
        return

    teachers[number - 1]["grades"].append(int(grade))
    save_teachers(teachers)
    print("Grade added!")


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
            print(f"\nTaskHub CLI - {FACULTY}")
            print("1 - Add teacher (add)")
            print("2 - Show teachers (show)")
            print("3 - Edit teacher (edit)")
            print("4 - Delete teacher (delete)")
            print("5 - Rate teacher (rate)")
            print("6 - Exit (exit)")

            choice = input("Choose command: ").strip().lower()

        if choice in COMMANDS:
            choice = COMMANDS[choice]

        if choice == "1":
            add_teachers = add_teacher(teachers)
        elif choice == "2":
            show_teachers(teachers)
        elif choice == "3":
            edit_teacher(teachers)
        elif choice == "4":
            delete_teacher(teachers)
        elif choice == "5":
            rate_teacher(teachers)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Unknown command!")

        if one_shot:
            break


if __name__ == "__main__":
    main()