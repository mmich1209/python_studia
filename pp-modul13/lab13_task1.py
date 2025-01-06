# # 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy
#
# #podnoszenie do potegi
# # **
#
# def potega(numbers, potega):
#     for i in numbers:
#         wynik = i ** potega
#         return wynik
#
# numbers = [1,2,3,4,5]
#
# print(potega(numbers,2))
#

def pow(numbers, exponent):
    numbers = numbers[:]  # zabezpieczenie przed modyfikacja listy
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


numbers = [1, 2, 3, 4, 5]
print(pow(numbers, 2))
print(pow(numbers, 2))
print(pow(numbers, 5))


def pow2(numbers, exponent):
    result = []
    for n in numbers:
        result.append(numbers[i] ** exponent)
    return result


def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]

# print(pow(numbers, 2))
print(pow2(numbers, 2))
# print(pow3(numbers, 2))
