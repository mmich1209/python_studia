#operatory logiczne
# and - koniunkcja, czytamy jak i
# or - alternatywa, czytamy jak lub
#not - negacja, czytamy jak nie

#iterujemy od 0 do 9 (10 iteracji)
#wyswietlamy cyfre, chyba ze:
#bedzie to liczba parzysta lub liczba wieksza od 6 to wyswietl gwiazdke *

for i in range(0,10):
    if i % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)

