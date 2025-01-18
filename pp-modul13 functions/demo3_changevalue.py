def change_value(n):
    print("przed zmiana", n)
    n += 1
    print("po zmianie,", n)  # to zmienia n tylko lokalnie, zmienna lokalna


value = 7  # zmienna globalnie
change_value(value)
print(value)

print("*" * 10)


#############

def change_value(my_list_1):
    my_list_1 = [0, 0]
    print(my_list_1)

my_list_2 = [1,2]
change_value(my_list_2)
print(my_list_2)


print("*" * 10)
#############

def change_value(my_list_1):
    my_list_1[0] = [99]
    print(my_list_1)


my_list_2 = [1, 2]
change_value(my_list_2)
print(my_list_2)

#to jest zmienna/wskaznik ktora wskazuje NA...
