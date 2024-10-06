#Ciag znakow
print("Ala ma kota, a kot ma Ale.")
print('Ala ma kota, a kot ma Ale.')

print("tekst ze \nznakiem nowej lini")

print("I'm Monthy Python.")
print('I\'m Monthy Python.') #tutaj \ to escape character

#jakie to sa znaki specjalne?
print("><", ">\t<", ">\t\t\t<")
print("><", ">\t<", ">\t\t\t<", sep="\n")

print("\\")
print("\\\\")
print("\\\\\\\\")

print(type(" "))

###### Wartosci logiczne (boolowskie)

print("False") #tutaj to jest string

print(False)

print(2 > 3 )   #otrzymamy odpowiedz logiczna, jest to false bo nie prawda
print(type(2 > 3))

print(2 < 9)
print(type(2 > 9))

###

print(bool(1))
print(bool(13))
print(bool(0))   #0 daje false, wszystko dodatnie daje tru)
