# pobranie 3 liczb od uzytkownika i wyswietlenie ich na ekranie

# print("Podaj Liczbe")
# a = int(input())
# print("Podaj Liczbe")
# b = int(input())
# print("Podaj Liczbe")
# c = int(input())
#
# print("Pobrano liczby: ", a, b, c)

# Popbranie 3 liczb od użytkownika i wyśiwietlnie ich na ekranie

# def show_message(number_no):
#     print("Proszę Podaj {} liczbę: ".format(number_no))
#
# show_message(1)
# a = int(input())
# show_message(2)
# b = int(input())
# show_message(3)
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

def get_number(number_no):
    print("Proszę Podaj {} liczbę: ".format(number_no))
    return int(input())

#zamiast tego ponizej, mozna uzyc od razu get number w innej funkcji
# a = get_number(1)
# b = get_number(2)
# c = get_number(3)

print("Pobrano liczby:", get_number(1), get_number(2), get_number(3))