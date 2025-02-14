class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        print("Cześć, jestem", self.__name, "i mam", self.__age, "lat/a")


persons = []
persons.append(Person("Janek", 23))
persons.append(Person("Tomek", 40))

for person in persons:
    person.introduce()