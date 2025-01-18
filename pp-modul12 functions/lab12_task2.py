# Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998

# def prostokąt(bok_a, bok_b):
#     pole = bok_a * bok_b
#     obwod = (2 * bok_a) + (2 * bok_b)
#     przekatna_kwadratu = (bok_a**2 + bok_b**2) ** 0.5
#     return pole, obwod, przekatna_kwadratu

def pole_prostokata(bok_a, bok_b):
    pole = bok_a * bok_b
    return pole

def obwod_prostokata(bok_a, bok_b):
    obwod = (2 * bok_a) + (2 * bok_b)
    return obwod

def przekatna_kwadratu(bok_a, bok_b):
    return (bok_a ** 2 + bok_b ** 2) ** 0.5

lista_wymiarow = [[4, 5],[2678, 5678],[344555, 788998]]

for i in range(0, len(lista_wymiarow)):
    print("Pole prostokata o wymiarach :", lista_wymiarow[i][0], lista_wymiarow[i][1], "wynosi: ",  pole_prostokata(lista_wymiarow[i][0], lista_wymiarow[i][1]))
    print("Obwod prostokata o wymiarach :", lista_wymiarow[i][0], lista_wymiarow[i][1], "wynosi: ",  obwod_prostokata(lista_wymiarow[i][0], lista_wymiarow[i][1]))
    print("przekatna prostokatu o wymiarach :", lista_wymiarow[i][0], lista_wymiarow[i][1], "wynosi: ",  przekatna_kwadratu(lista_wymiarow[i][0], lista_wymiarow[i][1]))


