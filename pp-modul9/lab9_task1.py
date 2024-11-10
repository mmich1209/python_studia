# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

zakres_poczatkowy = int(input("Podaj poczatkowy zakres zbioru: "))  # range_from
zakres_koncowy = int(input("Podaj koncowy zakres zbioru: "))  # range_to

is_first = True

# trzeba zwiekszyc zakres + 1 bo tak dziala petla for.
print("Liczby z zakresu od", zakres_poczatkowy, "do", zakres_koncowy, "podzielne przez 3 lub 5 lub 7 to:", end=" ")
for i in range(zakres_poczatkowy, zakres_koncowy + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end="")
    is_first = False
print(".")
