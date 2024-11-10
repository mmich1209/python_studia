denver = [1_700_000, 4_600_000, 2_100_000]

philadelphia = []  # pusta lista, do tej listy bedziemy dodawac elementy
philadelphia.append(1_800_000)
philadelphia.append(5_000_000)
philadelphia.append(2_500_000)

print(denver)
print(philadelphia)

total = [0, 0, 0]
total[0] = denver[0] + philadelphia[0]  # wartosc dla danego roku
total[1] = denver[1] + philadelphia[1]
total[2] = denver[2] + philadelphia[2]
print(total)

average = (total[0] + total[1] + total[2]) / len(total)

# formatowanie dodajmy
# "".format()
# "{:,d}" - d jest for decimal

print("Produkcja w roku 2012 wyniosła: ", "{:,d}".format(total[0]).replace(",", " "), "sztuk.")
print("Produkcja w roku 2013 wyniosła: ", total[1], "sztuk.")
print("Produkcja w roku 2014 wyniosła: ", total[2], "sztuk.")
print("Srednia produkcja wyniosla: ", "{:,.0f}".format(average).replace(",", " "), "sztuk.")

# "{:,.0f}" - chcemy 0 po przecinku. f oznacza float
# ("{:.02}".format(number))
