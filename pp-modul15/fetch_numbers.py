numbers = []
counter = 1

while True:
    if counter > 5:
        break
    try:
        number = int(input("Podczaj liczbe calkowita: "))
        numbers.append(number)
        counter += 1
    except:
        print("To nie jest liczba calkowita, spróbuj ponownie")

print(numbers)
