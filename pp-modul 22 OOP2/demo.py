class MyClass:
    def __init__(self, x=1): #to jest zmienna instancji, bo jest w srodku konstruktora
        self.x = x

    def sety(self,y):
        self.y = y
#jesli nie podamy wartosci to przyjmie sie wartosc domyslna, tj x=1

obj = MyClass(99)
obj.sety(77)

print(obj.x, obj.y)

obj2 = MyClass(0)
obj2.sety(0)

print(obj2.x, obj2.y)

obj3 = MyClass()
obj3.z = 1

print(obj3.x, obj3.z)

print(obj.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)

