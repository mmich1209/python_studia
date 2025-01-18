def count_down(wishes = True):
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")
    if not wishes:
        return
    print("Szczesliwego nowego roku!")

count_down(False)
#count_down(wishes=False) #to samo ale lepsze bo bardziej czytelne