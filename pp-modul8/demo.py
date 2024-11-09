# Uzywamy petli by wyswietlic cyfry

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1

# To samo za pomoca petli for # tutaj nie trzeba dodawac inkrementacji, bo tym sie zajmuje funkcja for
# for i in range(0, 10):
#     print(i, end=" ")

# for i in range(0, 10, 1):
#     print(i, end=" ")
#
# print("|")
#
# for i in range(10):
#     print(i, end=" ")

# To to samo, mozna podac tylko 1 argument.

# for i in range (3, 100, 13):
#     print(i, end=" ")

# Funkcja range daje nam takie mozliwosci ze poczatek jest 3, koniec <100, a krok skaczemy co 13


##### Tutaj liczymy w dol 9 8 7 6 ...
# for i in range(9, -1, -1):
#     print(i)
#
######## Petle przydaja sie do liczenia np silni. Silnia to operacja oznaczana wykrzyknikiem
# Czyli silnia 3!
# 3! = 1 * 2 * 3 = 6
#
# number = 5
# factorial = 1
#
# for i in range(1, number + 1):
#     factorial *= i
#     print(factorial)

# Teraz zrobmy to tylko z petla while



number = 5
factorial = 1

while number:
    factorial *= number
    number -= 1

print(factorial)




