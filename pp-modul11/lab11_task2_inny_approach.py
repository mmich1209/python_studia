numbers = []
numbers_total = int(input("Podaj liczbe elementow zbioru: "))

for i in range(numbers_total):
    number = int(input("Podaj " + str(i + 1) + " element zbioru: "))
    numbers.append(number)

numbers_without_duplicates = []   #pozbywanie sie duplikatow. Mozna uzyc tez set(), usuwa duplikaty
for number in numbers:
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)


numbers_without_duplicates.sort(reverse=True)
print(numbers_without_duplicates)
