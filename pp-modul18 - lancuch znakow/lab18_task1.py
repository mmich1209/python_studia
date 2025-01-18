# wyswietl polski alfabet

lista = ["a", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ń", "o", "ó", "p", "r", "s",
         "t", "u", "w", "y", "z", "ź", "ż"]

print("Litera --> Punkt Kodowy")
for letter in lista:
    print(letter, "-->", ord(letter))
