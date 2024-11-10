# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika

names_count = int(input("Podaj liczbe imion: "))
lista_imion = []

for i in range(names_count):
    imie = input("Podaj imie: ")
    lista_imion.append(imie)

print("Pelna lista imion podanych przez uzytkownika to", lista_imion)

#moze byc tez tak
# for i in range(names_count):
#       lista_imion.append(input("Podaj imie: "))
#
# print("Pelna lista imion podanych przez uzytkownika to", lista_imion)
