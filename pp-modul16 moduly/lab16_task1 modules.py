#  Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

import math
from random import sample
from platform import machine, processor

#Check the CPU
print(machine())
print(processor())

#Wylosuj 3 niepowtarzalne liczby
wylosowane_liczby = sample(range(11), 3)
print("Wylosowane liczby to: ", wylosowane_liczby)

#Wyznacz sinus 90 stopni
print(math.sin(math.radians(90)))