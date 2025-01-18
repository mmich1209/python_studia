#wylosuj dowolna liczbe liczb od 1 do 99

import random

def generate_nums(total_numbers):
    numbers = []
    for _ in range(total_numbers):
        numbers.append(random.randint(1, 99))
    return numbers


print(generate_nums(10))
print(generate_nums(100))