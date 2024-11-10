# . Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

# Rzut kostka - jakie sa mozliwe wyniki: 1, 2, 3, 4, 5, 6


import random
counter_szostek = 0
lista_rzutow = []
values_repeated = 0


for i in range(17):  # 16 rzutow
    random_number = random.randint(1, 6)
    lista_rzutow.append(random_number)
    if random_number == 6:
        counter_szostek += 1

print(lista_rzutow)
print("Rzut nr. 8 to: ", lista_rzutow[7])
print("Liczba rzutow o wartosci 6 to:", counter_szostek)

for i in lista_rzutow:
    if lista_rzutow[i] == lista_rzutow[i+1]:
        values_repeated += 1
print("Ilosc maxymalnych tych samych wartoisc pod rzad:", values_repeated)

# if i == i +1:
# values_repeated += 1

