class Animal:
    all_counter = 0

    def __init__(self, name):
        Animal.all_counter += 1

    def introduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name}, jest nas {self.counter}, a wszystkich zwierząt {self.all_counter}")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Dog.counter += 1


    def make_sound(self):
        return "hał hał hał"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Cat.counter += 1

    def make_sound(self):
        return "miauł miauł"

class Pig(Animal):
    type = "świnka"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Pig.counter += 1

    def make_sound(self):
        return "hrum hrum"

class Horse(Animal):
    type = "koń"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        Horse.counter += 1

    def make_sound(self):
        return "ihhaaa ihaaa"

animals = [
    Dog("Pluto"),
    Dog("Reksio"),
    Cat("Bruno"),
    Cat("Filemon"),
    Cat("Heban"),
    Pig("Puszek"),
    Horse("Szybki Bill"),
]

for animal in animals:
    animal.introduce()


