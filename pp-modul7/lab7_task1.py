# Napisz skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej
# pobranej od użytkownika jest także liczbą całkowitą

number = int(input("Podaj liczbe: "))

if number ** .5 % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie"

print(str1 + ", pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczba calkowita.")

