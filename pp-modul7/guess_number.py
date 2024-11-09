# This is a game. The script randomly chooses a number, the player must guess the number
import random  # importujemy generator randomowych liczb

number = random.randint(1, 4)
guess = int(input("Guess a number, od 1 do 4: "))

if guess == number:
    print("Congratulations! You guessed the number!")
else:
    print("Sorry, you lose! " "The number is: " + str(number) + ".")

