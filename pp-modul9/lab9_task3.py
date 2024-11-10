number = int(input("Podaj liczbę: "))
n = int(input("Podaj nr bitu: "))

#Najpierw wizualizujemy problem - wyswietlamy bity
print("{:08b}".format(number)) #8 bitow naszej liczby ktora pobierzemy od uzytkownika



#by wizolowac ten bit musimy zrobic maske
mask= 1 << n   #bierzemy bit i przesuwamy o n tyle ile chce
result = number & mask #uzywamy koniunkcji
bit = (int(bool(result)))

print("{:08b}".format(mask))
print("-" * 10)
print("{:08b}".format(result))

print("bit na pozycji", n, "dla liczby", number, "wynosi", bit)



