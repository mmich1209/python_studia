# fetch floating numbers
numbers = []
counter = 1

while True:
    if counter > 3:
        break
    try:
        number = float(input("Podaj {} liczbe zmiennoprzecinkowa: ".format(counter)))
        numbers.append(number)
        counter += 1
    except:
        print("Podana wartość jest niepoprawna, spróbuj ponownie!")

print(numbers)
