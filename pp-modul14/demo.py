numbers = (1, 2, 3 )   #krotka


print(numbers)
print(numbers[0])
print(numbers[-1])

for number in numbers:
    print(number)

print(numbers[1:])
####################

numbers = [x for x in range(10) if x % 2 == 0]
numbers = list(x for x in range(10) if x % 2 == 0) #tez mozna uzyc
print(numbers)

#roznica polega na tym ze zastepujemy to funkcja tuple
numbers = tuple(x for x in range(10) if x % 2 == 0)
print(numbers)

####do tupla nie mozna przypisywac wartosci

numbers = (1,2,3)

numbers[0] = 999 #da nam tuple object does not support item assignment

#del numbers[0] tez sie nie da
# mozna tylko usunac cala krotke del numbers

numbers = (1,2,3)
print(len(numbers))
print(numbers * 2) #to jest nowa krotka, jej kopia, powiekszona

########################
konwersja listy na krotke

numbers = [1,2,3]

print(numbers)
numbers = tuple(numbers)
print(numbers, type(numbers))

Zrob krotke z napisem ala ma kota
letters = tuple("Ala ma kota.")
print(letters)
