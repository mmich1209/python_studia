# phones = {"Tomek": 555666777, "Ada": 123123123, "Karol": 444333222}
# print(phones)
# # klucze nie moga sie powtarzac, klucz sluzy do jednoznacznej interpretacji wg klucza
# # gdy wprowazdimy znowu "Tomek" to sie nadpisze
#
# phones = {"Tomek": 555666777, "Ada": 123123123, "Karol": 444333222, "Tomek": 999999999}
# print(phones)
###########
##Animals dictionary

animals_dict = {
    'dog': 'pies',
    'cat': 'kot',
    'snake': 'waz'
}

print(animals_dict)
print(animals_dict.get('hamster', "Brak takiego klucza w slowniku"))

print(animals_dict.keys())

########

# words = ["kot", "lew", "chomik"]
#
# for word in words:
#     if word in animals_dict.keys():
#         print(word, "->", animals_dict[word])
#     else:
#         print("Nie znaleziono slowa {} w slowniku".format(word))

for key in animals_dict.keys():  # przez slownika nie mozna iterowac bezposrednio, trzeba uzyc keys
    print(key, "->", animals_dict[key])

for value in animals_dict.values():
    print(value)

# czyli mozna iterowac przez keys, przez values, ale tez przez cale elementy
# czyli items, a item to krotka wiec zobaczymy krotki
for item in animals_dict.items():
    print(item)  # mozemy tez uzyc print(key, value)
    print(key, value)

for pl, en in animals_dict.items():
    print(pl, "->", en)

###########

animals_dict["swinka"] = "pig"  #dodalismy wartosc
print(animals_dict)

### metoda pop item

print(animals_dict.popitem())
print(animals_dict)
#pop item pokazuje ostatnie i usuwa

##### wysprzatanie calego slownika animals

animals_dict.clear()
print(animals_dict)

