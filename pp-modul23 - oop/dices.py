import random


class Dice:
    def __init__(self):
        self.__value = None

    def throw(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return f"[{self.__value}]"


class DicePair(Dice):
    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw()
        self.__pair[1].throw()

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])

    def is_duble(self):
        return self.__pair[0]._Dice__value == self.__pair[1]._Dice__value



dices = DicePair()
while True:
    dices.throw()
    print(dices)
    if dices.is_duble():
        break



