#gra toczy sie dopoki nie zostanie odgadnieta liczba

# import random
# random_number = random.randint(1, 10)
# guess = int(input("Guess a number: "))
#
# if guess == random_number:
#     print("Wygrales za pierwszym raz!")
# else:
#     while guess != random_number:
#         guess = int(input("Zgaduj dalej: "))
#         if guess == random_number:
#             print("Wygrales")



import random

counter = 1
random_number = random.randint(1, 10)
guess = int(input("Guess a number: "))

while guess != random_number:
    guess = int(input("Zgaduj dalej: "))
    counter += 1

print("Brawo! Udalo ci sie juz za " + str(counter) + " razem.")
