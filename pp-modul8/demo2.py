# for i in range(5):
#     print(i)
# else:
#     print("Koniec petli")

# Jak damy break to else sie nie wykona

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Koniec petli")
