# # fruits = ["apple", "banana", "cherry"]
# # print(fruits)
# # print(len(fruits), fruits)
#
# # del fruits[0]
# # print(fruits)
# #
# # print("-" * 20)
# #
# # print(len(fruits), fruits)
#
# # Czy mozna usunac cala liste ? # usuwamy obiekt z pamieci, takze daje error "name fruits is not defined"
# # del fruits
# # print(len(fruits), fruits)
#
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits), fruits)
#
# print(len(fruits))  # len() to funkcja
#
# fruits.append("plum")  # append() to metoda
#
# print(fruits)
#
# #append dodaje na samym koncu. A co jesli chcemy wsadzic w innym miejscu ? Uzywamy insert
#
# fruits.insert(0, "orange")
# print(fruits)
#
# Iterowanie
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i])

print("--" * 10)

for fruit in fruits:
    print(fruit)


