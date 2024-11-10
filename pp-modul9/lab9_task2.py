# Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.

# zbiór=(1, 100)
counter = 0

for i in range(1, 101):
    if i % 2 == 0 and i > 90:
        print(i)
        counter += 1
    elif i % 2 != 0 and i % 9 == 0:
        print(i)
        counter += 1

print("Ilosc liczb z takimi warunkami to: " + str(counter))
