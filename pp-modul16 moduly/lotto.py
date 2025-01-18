""""This modul is for useful functions for lotto lottery."""
from random import sample


def draw_numbers():
    numbers = [i for i in range(1, 50)]
    lucky_numbers = sample(numbers, 6)
    lucky_numbers.sort()
    return (lucky_numbers)  # return sample(range(1, 50), 6) - 1 liner


def get_user_numbers():
    n = 6  # mamy te 6 liczb czy nie
    counter = 1
    user_numbers = []
    while counter <= n:
        try:
            take_number = int(input("Enter a {} number (1-49): ".format(counter)))
            if take_number in user_numbers:
                print("You have already entered this number")
                continue
            if take_number < 1 or take_number > 49:
                print("Liczba spoza zakresu. Podaj liczbe od 1 do 49.")
                continue
        except ValueError:
            print("To nie jest liczba całkowita.")
            continue
        user_numbers.append(take_number)
        counter += 1
    user_numbers.sort()
    return user_numbers


def check_user_numbers(user_numbers, lucky_numbers):
    counter = 0
    for number in user_numbers:
        if number in lucky_numbers:
            counter += 1
    return counter


if __name__ == '__main__':
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_user_numbers(user_numbers, lucky_numbers)

    print(user_numbers)
    print(lucky_numbers)
    print(result)
