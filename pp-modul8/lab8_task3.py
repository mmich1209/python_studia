# szachy
# Plansza do gry sklada sie z kratownicy 8*8
# 0 1 2 3 4 5... az do 64
# 1 2 4 8 16 32.... <- to jest 2 do potęgi

# r = wartosc ziarenek na polu
# suma
suma = 0

for i in range(0, 64):
    suma += (2 ** i)
    print(suma)

print("Suma wszystkich ziaren zboza na szachownicy: " + str(suma))

# zalozenia
# waga 1 ziarenka = 0.4mg -> 0.0004g
# 1kg = 1000g
# 1000kg = 1t

tons = int(suma * 0.0004 / 1000 / 1000)

print("To bedzie ton: ", tons)

#roczna produkcja pszenicy na swiecei to 782 mln ton
years = int(tons / 782_000_000)
print("Na ile lat starczy calemu swiatu tej pszenicy: ", years)
