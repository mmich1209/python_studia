# a = 1
# b = 4
#
# print("a = ", a, "b = ", b)
#
# a, b = b, a    #odwaracamy jednolinijkowo mozna to zrobic
#
# print("a = ", a, "b = ", b)
#
# #Kiedy to pomocne? Np przy operowaniu na listach
#
# numbers = [1, 2 ,3 ]
# print(numbers)
# numbers[0], numbers[1] = numbers[1], numbers[0]
# print(numbers)

### sortowanie

# numbers = [4, 5, 2, 1, 4, 5, 9, 8, 88, 99]
#
# numbers.sort()
# print(numbers)
#
# ### sortowanie odwrotne
#
# numbers.sort(reverse=True)
# print(numbers)
#
#
# #### litery tez sortuje
# letters = ["C", "A", "B", "F"]
# letters.sort()
# print(letters)
#
# letters.sort(reverse=True)
# print(letters)
############

list_1 = [9]
list_2 = list_1 #kopiuje nazwe listy, ale NIE jej zawartosc
#2 nazwy wskazujace na 1 liste
list_2[0] = 13
print(list_1)

