# Napisz skrypt symulujący grę losową:
# • użytkownik obstawia 6 liczb z 49,
# • program losuje 6 liczb z 49,
# • użytkownik dostaje informacje o ilości trafień

import random

obstawione_liczby = []
ilosc_liczb = 6
hit_total = 0
while ilosc_liczb > 0:
    liczba = int(input("Podaj 6 liczb od 1 do 49:"))
    ilosc_liczb -= 1
    obstawione_liczby.append(liczba)

print("Oto obstawione liczby: ", obstawione_liczby)

wylosowane_liczby = random.sample(range(1,50), 6)  #musi byc range, i 3ci argument to jest ile tych liczb

print("Oto wylosowane liczby: ", wylosowane_liczby)

for i in obstawione_liczby:
    if i in wylosowane_liczby:
        print("Tak! Ta liczba", i, "zostala wylosowana. Gratulacje!")
        hit_total += hit_total + 1
    else:
        print("Niestety ta liczba", i, "nie zostala wylosowana.")

print("Zostalo trafionych: " +str(hit_total) + " liczb")

