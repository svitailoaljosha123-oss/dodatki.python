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

if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as file:
        teachers = json.load(file)
else:
    teachers = []


def save():
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(teachers, file, ensure_ascii=False, indent=4)


def average(teacher):
    if len(teacher["grades"]) == 0:
        return None
    return sum(teacher["grades"]) / len(teacher["grades"])


def show_names():
    for i in range(len(teachers)):
        print(f"{i + 1}. {teachers[i]['name']}")



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
        name = input("Enter teacher full name: ").strip()

        if name == "":
            print("Name cannot be empty!")
        else:
            teacher = {
                "name": name,
                "faculty": FACULTY,
                "grades": []
            }

            teachers.append(teacher)
            save()

            print("Teacher added!")


    elif choice == "2":
        if len(teachers) == 0:
            print("No teachers.")
        else:
            print(f"\nTeachers ({FACULTY}):")

            for i in range(len(teachers)):
                avg = average(teachers[i])

                if avg is None:
                    rating = "no grades"
                else:
                    rating = f"{avg:.2f} / 5 ({len(teachers[i]['grades'])} grades)"

                print(f"{i + 1}. {teachers[i]['name']} - {rating}")


    elif choice == "3":
        if len(teachers) == 0:
            print("No teachers.")
        else:
            show_names()

            number = input("Enter teacher number: ")

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(teachers):
                    new_name = input("Enter new name: ").strip()

                    if new_name == "":
                        print("Name cannot be empty!")
                    else:
                        teachers[number - 1]["name"] = new_name
                        save()

                        print("Teacher changed!")
                else:
                    print("Wrong teacher number!")
            else:
                print("Enter a number!")


    elif choice == "4":
        if len(teachers) == 0:
            print("No teachers.")
        else:
            show_names()

            number = input("Enter teacher number: ")

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(teachers):
                    teachers.pop(number - 1)
                    save()

                    print("Teacher deleted!")
                else:
                    print("Wrong teacher number!")
            else:
                print("Enter a number!")


    elif choice == "5":
        if len(teachers) == 0:
            print("No teachers.")
        else:
            show_names()

            number = input("Enter teacher number: ")

            if number.isdigit():
                number = int(number)

                if 1 <= number <= len(teachers):
                    grade = input("Enter grade (1-5): ")

                    if grade.isdigit() and 1 <= int(grade) <= 5:
                        teachers[number - 1]["grades"].append(int(grade))
                        save()

                        print("Grade added!")
                    else:
                        print("Grade must be a number from 1 to 5!")
                else:
                    print("Wrong teacher number!")
            else:
                print("Enter a number!")


    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Unknown command!")


    if one_shot:
        break