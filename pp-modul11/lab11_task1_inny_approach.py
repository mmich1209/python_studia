user_numbers = []
random_numbers = []
hit_total = 0

import random

for i in range(6):
    user_numbers.append(int(input("Podaj " + str(i + 1) + " liczbe od 1-49: ")))

random_numbers = random.sample(range(1, 50), 6)

for numbers in user_numbers:
    if number in random_numbers:

