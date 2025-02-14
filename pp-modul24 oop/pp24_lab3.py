class Employee:
    def __init__(self, name, position):
        self.__name = name
        self.__position = position

    def introduce(self):
        return f"Cześć, jestem {self.__name}, moja pozycja to {self.__position}."

    def get_name(self):
        return self.__name


class Manager(Employee):
    def __init__(self, name, project):
        super().__init__(name, "Manager")  # Przekazujemy "Manager" jako pozycję
        self.__project = project

    def introduce(self):
        return f"{super().introduce()} Prowadzę projekt: {self.__project}."


class Worker(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Pracownik")  # Przekazujemy "Pracownik" jako pozycję
        self.__salary = salary

    def introduce(self):
        return f"{super().introduce()} Moje wynagrodzenie to {self.__salary} zł."


class Person(Employee):
    def __init__(self, name):
        super().__init__(name, "Osoba")  # Przekazujemy "Osoba" jako pozycję

    def introduce(self):
        return f"{super().introduce()} Nie posiadam wynagrodzenia ani projektu."


# Lista różnych osób/pracowników
people = [
    Manager("Jan Kowalski", "Projekt X"),
    Worker("Anna Nowak", 5000),
    Person("Marek Wiśniewski"),
    Manager("Ewa Kaczmarek", "Projekt Y"),
    Worker("Piotr Zieliński", 4500),
    Person("Kasia Nowak")
]

# Prezentacja danych
for person in people:
    print(person.introduce())
