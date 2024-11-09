# 3. Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać 3 szanse.
# Po nieudanej próbie, gracz powinien otrzymać podpowiedź np. o parzystości zgadywanej liczby itp.

import random

number = random.randint(1, 10)
msg = "Zgadnij jaka liczbe mam na myśli od 1 do 10: "
guess = int(input(msg))

if guess == number:
    print("Brawo. Taką liczbe miałem na myśli")
else:
    msg = "Masz kolejną szansę, moja liczba jest "
    if number % 2 == 0:
        msg += "parzysta: "
    else:
        msg += "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Brawo! Odgadłeś za drugim razem.")
    else:
        msg = "Masz ostatnią szansę, moja liczba jest "
        if number > 5:
            msg +="większa niż"
        else:
            msg +="mniejsza lub równa"
        msg +="pięć: "
        guess = int(input(msg))
        if guess == number:
            print("Brawo! Zgadłeś za 3 razem")
        else:
            print("NIestety myślałem o liczbie " + str(number) + ".")