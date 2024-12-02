#wylosuje 3 liczby ze zbioru 1-10, bez powtorzen, posortuj wynik

import random
numbers = [i for i in range(1,11)]
random_numbers = random.sample(numbers, 3)
print(random_numbers)


