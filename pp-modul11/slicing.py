# wycinki (slicing)
# lista[start:end] #end to jest indeks koncowy -1

numbers = [10, 8, 6, 4, 2]

new_numbers = numbers[-4:-1]
print(new_numbers)

new_numbers = numbers[1:4]
print(new_numbers)

# np mozemy nie znac dlugosci i dac

new_numbers = numbers[:-2: len(numbers) - 1]
print(new_numbers)



# [:] kopiowanie calej listy


