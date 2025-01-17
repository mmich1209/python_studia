#ksiazka telefoniczna
#

ksiazka_telefoniczna = {
    "Tomek": 555666777,
    "Ada": 123123123,
    "Karol": 444333222,
    "Ania": 999999999

}

while True:
    imie = input("Podaj imię: ")
    if imie == "":
        break
    if imie in ksiazka_telefoniczna:
        print("Telefon:", ksiazka_telefoniczna[imie])
    else:
        print("Nie znaleziono telefonu dla imienia", imie)

