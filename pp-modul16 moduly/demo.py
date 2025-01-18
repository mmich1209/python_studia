import modul #importujemy ten nasz pliczek modul.py

# print(dir(modul))
#modul
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'is_string', 'sum_list_elem']#
#na koncu sa te nasze funkcje jak widac
#ale jak puscimy to teraz sie nie pusci ten test - bo zaimporotwalismy ten modul

# help(modul)

print("Czy to jest ciąg znaków? ", modul.is_string("test"))
print("suma elementów listy: ", modul.sum_list_elem([1,2,3]))

#no i nigdzie sie nam nie wyswietlil ten test co jest w modul. Takze to jest to zabezpieczenie

print(modul.__name__)
print(__name__)

# def check_numbers(list):
#     for number in list:
#         if not isinstance(number, int):  # TO SPRAWDZA WLASNIE JAKI JEST TYP, to co zawsze mysle jak zrobic z type()...
#             return False
#         else:
#             return True






