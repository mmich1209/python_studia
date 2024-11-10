# Zsumuj wszystkie elementy
total = 0

numbers = [1, 3, 55, 3, 2, 5, 71, 12, 33]

for number in numbers:
    total += number

print(total)

print("Suma wszystkich elementow listy", numbers, "to", str(total) + ".")

#mozna uzyc funkcji suma

print(sum(numbers))


print("Suma wszystkich elementow listy", numbers, "to", sum(numbers))