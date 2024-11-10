import random

DICE_ROLLS_TOTAL = 16
rolls = []

for i in range(DICE_ROLLS_TOTAL):
    rolls.append(random.randint(1, 6))

print("Zbiór wynikow po ", DICE_ROLLS_TOTAL, "rzutach kostką do gry to: " + str(rolls))
print("Rzut nr. 8 to: ", rolls[8 - 1])  # bo indeksy zaczynaja sie od 0

six_counter = 0
for roll in rolls:
    if roll == 6:
        six_counter += 1
print("Wyrzucono " + str(six_counter) + " szostek.")

# maksymalną liczbę wyrzuconych tych samych wartości pod rząd
# zmienne tymczasowe
# zmienne calkowite
# zmienna ktora okresla co to jest za wartosc
# zmienna ktora okresla ile razy

in_row_value_tmp = rolls[0]  # ustawiam na pierwszej liczbie, od czegos musze zaczac.
in_row_total_tmp = 0

in_row_value = rolls[0]
in_row_total = 0

for roll in rolls:
    if roll == in_row_value:
        in_row_total_tmp += 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp = 1
    if in_row_total_tmp > in_row_total:
        in_row_value = in_row_value_tmp
        in_row_total_tmp = in_row_total_tmp

print("Pod rzad wyrzucono: ", in_row_total, "razy wartosc,", in_row_value, ".")

