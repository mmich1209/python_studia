# Pobieramy od uzytkownika dlugosci 3 odcinkow
# Sprawdz czy z tych odcinkow mozemy stworzc trojkat
# Sprawdz jaki to bedzie trojkat ze wzgledu na boki (równoramienny, różnoboczny, równoboczny)
# Sprawdz jaki to bedzie trojkat ze wzgledu na katy (prostokatny, ostrokątny, rozwartokątny)

print("Podaj dlugosci 3 odcinkow (liczby calkowite)")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and b + c > a and c + a > b:
    print("Mozna zbudowac trojkat z takimi bokami,", end=" ")
    if a == b and a == c and b == c:  # lancuchowy operator porownania a == b == c
        print("Powstanie trojkat rownoboczny")
    elif a == b or a == c or b == c:
        print("powstanie trojkat rownoramienny")
    else:
        print("powstanie trojkat różnoboczny")
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print("Powstanie trojkat prostokątny")
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
        print("Powstanie trojkat rozwartokątny")
    else:
        print("powstanie trojkat ostrokątny")
else:
    print("Z tych odcinkow nie mozna zbudowac trojkata")
