# Ciąg Fibonacciego to ciąg liczb naturalnych, w którym każda kolejna liczba jest sumą dwóch poprzednich12345.
# Pierwsza liczba ciągu to F0 = 0, a druga F1 = 11. Sekwencje Fibonacciego zazwyczaj mają F0 = 0, F1 = 1 i F2 = 13.
# W ciągu liczb Fibonacciego pierwsze dwa wyrazy zawsze są równe jedynce,
# a następnie każda kolejna wartość powstaje jako suma dwóch poprzednich liczb5.
# 1 1 2 3 5 8 ...

# Podaj mi 1wszy element ciagu Fibonacciego
# Podaj mi 1045 element itd

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    element_1 = element_2 = 1
    sum = 0

    for i in range(3, n + 1):
        sum = element_1 + element_2
        element_1, element_2 = element_2, sum
    return sum

print(fib(100))

###################################### mozna to zrobic w rekurencji