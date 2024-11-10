a = 1
b = 4

print("a = ", a, "b = ", b)

a, b = b, a    #odwaracamy jednolinijkowo mozna to zrobic

print("a = ", a, "b = ", b)

#Kiedy to pomocne? Np przy operowaniu na listach

numbers = [1, 2 ,3 ]
print(numbers)
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)

