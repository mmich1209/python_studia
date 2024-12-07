#zsumuj wszystkie elementy listy

def sum_numbers(numbers):   #to lista
    sum = 0
    for number in numbers:
        sum += number
    return sum

numbers = [1,2,3,4,5]
print(sum_numbers(numbers))