# Napisz program wypisujacy w jednej linii oddzielone przecinkami wszystkie liczby parzyste ze zbioru 1 do 100

zbior_liczb = [i for i in range(1, 101) if i % 2 == 0]

for i in zbior_liczb:
    if i == zbior_liczb[-1]:
        print(str(i), end="")
    else:
     print(str(i) + ",", end="")

