# zysk z 3 letniej lokaty bankowej wg założeń:
# • inwestowane środki 46 567,00 zł
# • stałe percentage yearly 7.5%
##• coroczna kapitalizacja odsetek
# • w obliczeniach zastosuj złożony operator przypisani

amount = 46_567
percentage_yearly = 0.075

print("year1")
amount += (amount * percentage_yearly)
print("Po pierwszym roku", amount)

print("year2")
amount += (amount * percentage_yearly)
print("Po drugim roku", amount)

print("year3")
amount += (amount * percentage_yearly)
print("Po trzecim roku:", amount)

print("Zysk inwestycji po 3 latach to:", amount - 46_567)



