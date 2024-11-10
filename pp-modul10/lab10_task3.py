# digit counter
digits = [1, 2, 3, 3, 4, 1, 2, 3]
frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for digit in digits:
    frequency[digit] += 1

print(digits)
print(frequency)

most_common = 0
for i in range(len(frequency)):
    if frequency[i] > frequency[most_common]:
        most_common = i

print("Najczesciej wystepujaca cyfra jest: ", str(most_common))
print("Wystapila", frequency[most_common], "razy.")
