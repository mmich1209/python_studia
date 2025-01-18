# napisz funkcje ktora bedzie potrafila zamieniac klucze na wartosci w przekazanym do niej sliowniku
#
# przyklad
# print(reverse_dict{'a': 1, "b":2 })
# 1: a, 2:b

def reversing_function(user_dict):
    new_dict = {}
    for key_old, value_old in user_dict.items():
        new_dict[value_old] = key_old
    return new_dict

print(reversing_function({"a": 1, "b": 2, "c": 3}))

