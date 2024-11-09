# Skrypt pobiera liczbe od uzytkownika
# Wyswietla informacje czy dana liczba jest parzysta, i czy jest podzielna przez 5 i 7


liczba = int(input("Podaj: "))

if liczba % 2 == 0:
    print("Podana liczba jest parzysta")
else:
    print("Podana liczba jest nieparzysta")

if liczba % 5 == 0:
    print("Podana liczba dzieli sie przez 5")
else:
    print("Podana liczba nie dzieli sie przez 5")

if liczba % 7 == 0:
    print("Podana liczba dzieli sie przez 7")
else:
    print("Podana liczba nie dzieli sie przez 7")
