# Napisz program, który:
#
# Wygeneruje 50 losowych liczb z zakresu od 1 do 10. DONE
# Zliczy ich wystąpienia przy użyciu collections.Counter.
# Obliczy sumę wszystkich liczb przy pomocy sum.
# Znajdzie liczbę, która występuje najczęściej.
# Znajdzie największą liczbę w wygenerowanym zbiorze.

import random
zakres_liczb = []  #tworzymy pusta liste i bedziemy do niej dodawac

for i in range(50):         #bo chcemy 50 losowych liczb
    losowa_liczba = random.randint(1,10)
    zakres_liczb.append(losowa_liczba)

print(zakres_liczb)
print(f"Ilosc liczb to", len(zakres_liczb))

#task 2
from collections import Counter

licznik = Counter(zakres_liczb)
print("ilosc wystapien liczb to:", licznik)

# most_common = licznik.most_common(1)
most_common = Counter(zakres_liczb).most_common(1)
print("Najczesciej wystepujaca liczba to", most_common)


#task 3
## Obliczy sumę wszystkich liczb przy pomocy sum.
total_value = sum(zakres_liczb)
print(total_value)

#task 4
#najwieksza liczba
print(max(zakres_liczb))
