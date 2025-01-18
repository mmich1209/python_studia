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

weight_kg = float(input("Podaj wage w kilogramach: "))
height_cm = float(input("Podaj wzrost w metrach: "))


def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / height_cm ** 2
    return bmi


def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi < 25:
        return "waga prawidłowa"
    elif bmi < 30:
        return "nadwaga"
    else:
        return "otyłość"


bmi = calculate_bmi(weight_kg, height_cm * .01)
category = determine_bmi_category(bmi)

print("Wskaznik BMI: ", round(bmi, 2))
print("Kategoria: ", category)