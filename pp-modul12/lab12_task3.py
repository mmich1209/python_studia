# Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji


# BMI = masa ciała / wzrost²
#
# Innymi słowy: masa ciała / wzrost x wzrost.
# Należy też pamiętać o odpowiednich jednostkach. Wzrost zawsze podajemy w metrach, a więc nie 173, ale 1.73. Wagę podajemy zawsze w kilogramach.

waga = float(input("Podaj wage w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))

def bmi(waga,wzrost):
    bmi = waga / wzrost**2
    return bmi

print(bmi(waga,wzrost))