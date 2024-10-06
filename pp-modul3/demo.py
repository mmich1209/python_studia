print(0b1101) # literal w systemie dwojkowym
print(0o177) # literal w systemie 8mkowym
print(0xFF) # literal w systemie 16tkowym

print(0b01)

print("'type()' podaje klase")
print(type(2224))
print(type("xd"))

print("mozna mieszac te systemy")
print(0o12 + 0xA)
print(0b11 + 1)

print(type(0b11 + 1))

## Liczby zmiennoprzecinkowe. To jest kropka a nie przecinek
print(2.0) #kropka a nie przecinek
print(2,0) #zapis nie wyrzuci bledu, ale tutaj python czyta to jakos 2 liczby calkowite


# Notacja wykladnicza, naukowa

print(5e3) #to jest 5 * 10 **3        ** to znak potegi
print(1e17)





print(123_000_00)    #chcemy wyprintowac 123mln w funkcji wykladniczej
print("{:.2e}".format(123_000_000))     #uzywamy nawiasow klamrowych, jesli jest jeden argument wystarczy dwukropek, znaczy ze chodzi o liczbe float, 2 znaczy ile liczb po przecinku, e ze o wykladnicza)


#
print(2.3e-5)   #2 przecinek 3 razy 10 do minus 5 potegi
print("{:.6f}".format(2.3e-5))   #dwukropek bo jeden argument, kropka bo chodzi o float, 6 bo 6 miejsc po przecinku, f bo chcemy float a nie exponentialy)










