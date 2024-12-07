# Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.

zbior_liczb_usera = []
while True:
    input_usera = input("Podaj liczbę całkowitą. Jeśli chcesz skończyć podawać liczby naciśnij Enter: ")
    if input_usera == "":
        break
    else:
        liczba = int(input_usera)
        # Dodajemy liczbę tylko jeśli nie ma jej jeszcze w liście
        if liczba not in zbior_liczb_usera:
            zbior_liczb_usera.append(liczba)

zbior_liczb_usera.sort()
print(zbior_liczb_usera)

