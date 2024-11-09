# #Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
# otrzymanych punków z kolokwium

ilosc_punktow = int(input("Podaj ile punktow otrzymal uczen: "))

if ilosc_punktow >= 95:
    print("Ocena bardzo dobry 5 ")
elif ilosc_punktow > 84:
    print("Ocena ponad dobra 4.5")
elif ilosc_punktow >= 70:
    print("Ocena dobra 4")
elif ilosc_punktow > 60:
    print("ocena dosc dobry 3.5")
elif ilosc_punktow > 50:
    print("ocena dostateczny 3")
elif ilosc_punktow <= 50:
    print("ocena niedostateczny 2.0")
