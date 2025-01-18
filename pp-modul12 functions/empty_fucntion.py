#jesli zrobimy empty i nie bedziemy jeszcze wiedziec co w niej zawrzec

def empty_function():
    pass
print(empty_function())

##Mozemy tez sprawdzic czy wynikiem funkcji nie jest none

if empty_function() is None:   #is None == None
    print("Funkcja nic nie zwrocila.")