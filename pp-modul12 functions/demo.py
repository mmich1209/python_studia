# name = input("Enter your name: ") #funckaj input do ktorej prezkazalismy argument jako ciag znakow,
# ## i to zwrocilo ciag znakow
#
# print("Witaj! {}".format(name))
#

def introduce(first_name="Arek", last_name="Stoszek"):
    print("Czesc, jestem", first_name, last_name + ".")
introduce()
introduce("mati")
introduce(last_name="koks")
introduce("Mati","Koks")
introduce(last_name="Koks",first_name="Mati")


print("raz", "dwa", "trzy", sep="-")
