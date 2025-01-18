while True:
    try:
        number = int(input("Podaj liczbe calkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ValueError:
        print("To nie jest liczba calkowita.")
    except ZeroDivisionError:
        print("Błąd dzielenia przez zero")
    except:
        print("Coś poszlo nie tak...")
