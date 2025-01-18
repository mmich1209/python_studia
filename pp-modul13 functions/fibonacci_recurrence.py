# 1 1 2 3 5 8 ...

# Podaj mi 1wszy element ciagu Fibonacciego
# Podaj mi 1045 element itd

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n-2)


print(fib(100))