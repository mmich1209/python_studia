from lotto import get_user_numbers, draw_numbers, check_user_numbers

print("Witaj w grze LOTTO!")

# print(dir())

user_numbers = get_user_numbers()
print("Pobrane liczby to: ", user_numbers)

print(("\nNacisnij enter aby dokonac losowania liczb.\n"))
input()
lucky_numbers = draw_numbers()
print("Wylosowano liczby: ", lucky_numbers)

result = check_user_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("BRAWO, TRAFIONO 6 LICZB!")
elif result == 5:
    print("TRAFIONO 5 LICZB!")
elif result == 4:
    print("TRAFIONO 4! Niezla kasa")
elif result == 3:
    print("Trafiles 3!")
elif result == 2:
    print("Trafiles tylko 2")
elif result == 1:
    print("Trafiles tylko 1")
elif result == 0:
    print("Nic nie trafiles")
