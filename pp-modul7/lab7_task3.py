# gra w zgadywanie od 1 do 10

import random

random_number = random.randint(1, 100)
number = int(input("Zagrajmy w gre. Zgadnij jaka liczbe mam na mysli od 1 do 100: "))
if random_number == number:
    print("Wow, zgadles!")
elif random_number % 2 == 0:
    print("Nie zgadles. Masz podpowiedz - liczba jest parzysta")
elif random_number % 2 != 0:
    print("Nie zgadles. Masz podpowiedz - liczba jest nieparzysta")

number = int(input("Zgaduj jeszcze raz: "))
if random_number == number:
    print("Wow, zgadles!")
elif random_number > 50:
    print("Kolejna podpowiedz, numer jest wiekszy niz 50")
elif random_number < 50:
    print("Kolejna podpowiedz, numer jest mniejszy niz 50")

number = int(input("Zgaduj jeszcze raz: "))
if random_number == number:
    print("Wow, zgadles!")
elif random_number % 5 == 0:
    print("Kolejna podpowiedz, liczba jest podzielny przez 5")
else:
    print("Liczba nie jest podzielna przez 5")

number = int(input("Zgaduj jeszcze raz: "))
if random_number == number:
    print("Wow, zgadles!")
else:
    print("Niestety przegrales")

print("Liczba o ktorej myslalem to: " + str(random_number))
