# Napisz skrypt, który oblicza ile warta byłaby inwestycja na kwotę
# 14 000 zł, gdyby jej wartość zwiększyła się w pierwszym roku o 40%, w
# drugim roku zanotowała stratę w wysokości 1500 zł, a w trzecim roku
# zwiększyła się o 12%.

print("Początkowa wartość inwestycji:", 14_000)

print("Po pierwszym roku:")
print(14_000 * 1.4)

print("Po drugim roku:")
print((14_000 * 1.4) - 1500)

print("Po trzecim roku:")
print((((14_000 * 1.4) - 1500)) * 1.12)
