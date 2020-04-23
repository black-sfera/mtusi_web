groupmates = [
    {

        "name": "Иришка",

        "surname": "Михайловская",

        "exams": ["Информатика", "ЭЭиС", "Web"],

        "marks": [4, 3, 4]

    },
    {

        "name": "Катюша",

        "surname": "Миролюбова",

        "exams": ["История", "АиГ", "КТП"],

        "marks": [3, 3, 3]

    },
    {

        "name": "Сашуля",

        "surname": "Малейчик",

        "exams": ["Философия", "ИС", "КТП"],

        "marks": [5, 4, 5]

    },
    {

        "name": "Катюша",

        "surname": "Волкова",

        "exams": ["История", "АиГ", "КТП"],

        "marks": [4, 4, 5]

    },
    {

        "name": "Таисия",

        "surname": "Бун",

        "exams": ["Философия", "ИС", "КТП"],

        "marks": [5, 5, 5]

    }
]


def print_students(students):
    print(u"Имя".ljust(15),
          u"Фамилия".ljust(15),
          u"Экзамены".ljust(30),
          u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(15),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


def average_score(student):
    average_score = 0
    for mark in student["marks"]:
        if average_score == 0:
            average_score = mark
        else:
            average_score = (average_score + mark) / 2
    return average_score


def sorting_and_print_students_by_average_score(students, average_mark):
    print(u"Средний балл выше ", average_mark)
    print(u"Имя".ljust(15),
          u"Фамилия".ljust(15),
          u"Экзамены".ljust(30),
          u"Оценки".ljust(20))
    for student in students:
        if average_score(student) >= average_mark:
            print(student["name"].ljust(15),
                  student["surname"].ljust(15),
                  str(student["exams"]).ljust(30),
                  str(student["marks"]).ljust(20))


average_mark = int(input("average_mark: "))


print_students(groupmates)
print("\n")
sorting_and_print_students_by_average_score(groupmates, average_mark)
