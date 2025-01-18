"""This is my first module..."""


def is_string(val):
    """Simple string value validator."""
    return isinstance(val, str)  # sprawdzi instancje classsy string


def sum_list_elem(lst):
    sum = 0
    for elem in lst:
        sum += elem
    #    print(sum)
    return sum


print(dir())
print(__name__)

if __name__ == '__main__': #zabezpiecza nas ze jesli ktos zaimportje ten kod, to on sie mu nie pusci, tzn ten test
    print(is_string('abc') == True)
    print(is_string(133) == False)
    print(sum_list_elem([1, 1, 1]) == 3)
    print(sum_list_elem([]) == 0)
    print(sum_list_elem([]) == 0)
