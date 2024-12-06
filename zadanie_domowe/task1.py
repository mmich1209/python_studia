# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

# 1 pobranie liczby
zbior_liczb_usera = []

while True:
    input_usera = input("Podaj liczbe całkowitą. Jesli chcesz skończyc podawać liczby naciśnij Enter:")
    if input_usera == "":
        break
    else:
        zbior_liczb_usera.append(int(input_usera))
        continue

print("Ilosc podanych liczb to", str(len(zbior_liczb_usera)) + ("."), "Podane liczby to:", str(zbior_liczb_usera) + ".")
suma_liczb_parzystych = 0
suma_liczba_nieparzystych = 0

# teraz przeiterowac przez liste i sprawdzic czy dana liczba jest
for i in range(len(zbior_liczb_usera)):
    if zbior_liczb_usera[i] % 2 == 0:
        suma_liczb_parzystych += zbior_liczb_usera[i]

    else:
        suma_liczba_nieparzystych += zbior_liczb_usera[i]

print("Suma liczba parzystych:", suma_liczb_parzystych)
print("Suma liczba nieparzystych:", suma_liczba_nieparzystych)
