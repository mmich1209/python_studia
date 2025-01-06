# Elektroniczny dziennik z ocenami studentow
# - wprowadzanie ocen
# - wyswietlanie ocen wraz z wprowadzona srednia
# students = {"Tomek": tutaj damy liste
# students = {"Tomek": [lista z ocenami], "Agata": []}
# students = {"Tomek": [2,3 4], "Agata": [5,5,5]}

# wprowadzanie ocen - jakos trzeba pobrac te dane

def get_data():
    students = {}
    while True:
        student = input("Podaj imie studenta: ")
        if student == "":
            break
        mark = float(input("Podaj ocene: "))
        if mark < 2 or mark > 5:
            break

    if student in students:
        marks = student[student]
        marks.append(mark)
    else:
        marks = [mark]
    students.update({student: marks})

    return students


def print_summary(students):
    pass


# print_summary(get_data())
print(get_data())
