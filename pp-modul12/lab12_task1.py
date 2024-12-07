# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie

def print_character(character, how_many_times, horizontal):
    if horizontal == True:
        print(character * how_many_times, end="")
    else:
        print((character + "\n") * how_many_times)


# print_character("A", 3, True)

print_character("XD", 15, False)
