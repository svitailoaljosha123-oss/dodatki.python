import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(BASE_DIR, "teachers.json")
FACULTY = "Математичний факультет"



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


def choose_teacher(teachers):
    """Показує список і просить обрати номер.
    Повертає індекс викладача або None, якщо ввід неправильний."""
    show_names(teachers)
    number = input("Enter teacher number: ")

    if not number.isdigit():
        print("Enter a number!")
        return None

    number = int(number)
    if not (1 <= number <= len(teachers)):
        print("Wrong teacher number!")
        return None

    return number - 1




def add_teacher(teachers):
    name = input("Enter teacher full name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    teachers.append({
        "name": name,
        "faculty": FACULTY,
        "grades": []
    })
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

    index = choose_teacher(teachers)
    if index is None:
        return

    new_name = input("Enter new name: ").strip()

    if new_name == "":
        print("Name cannot be empty!")
        return

    teachers[index]["name"] = new_name
    save_teachers(teachers)
    print("Teacher changed!")


def delete_teacher(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    index = choose_teacher(teachers)
    if index is None:
        return

    teachers.pop(index)
    save_teachers(teachers)
    print("Teacher deleted!")


def rate_teacher(teachers):
    if len(teachers) == 0:
        print("No teachers.")
        return

    index = choose_teacher(teachers)
    if index is None:
        return

    grade = input("Enter grade (1-5): ")

    if not (grade.isdigit() and 1 <= int(grade) <= 5):
        print("Grade must be a number from 1 to 5!")
        return

    teachers[index]["grades"].append(int(grade))
    save_teachers(teachers)
    print("Grade added!")


def show_top(teachers):
    """Показує рейтинг викладачів від найкращого середнього балу."""
    rated = [t for t in teachers if average(t) is not None]

    if len(rated) == 0:
        print("No rated teachers yet.")
        return

    rated.sort(key=average, reverse=True)

    print(f"\nTop teachers ({FACULTY}):")
    for place, teacher in enumerate(rated, start=1):
        print(f"{place}. {teacher['name']} - {average(teacher):.2f} / 5")
