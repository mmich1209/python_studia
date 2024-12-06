# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum,
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
# użytkownika,
# • wyświetli wylosowane serie liczb.

# ile serii liczb
# jaki zakres
# ile liczb wylosowac w danej serii

import random

liczba_serii = 0
ile_liczb_w_serii = 0
zakres_min = 0
zakres_max = 0

liczba_serii = int(input("Podaj ile serii liczb chcesz wylosowac:"))
ile_liczb_w_serii = int(input("Podaj ile liczb w serii chcesz wylosowac:"))
zakres_min = int(input("Podaj zakres minimalny:"))
zakres_max = int(input("Podaj zakres maxymalny:"))

wszystkie_serie = []

current_seria = []
for i in range(liczba_serii): #czyli tyle razy ile podał tworzymy nowa mini liste
    current_seria = [random.randint(zakres_min, zakres_max) for i in range(ile_liczb_w_serii)]
    wszystkie_serie.append(current_seria)

print(wszystkie_serie)


