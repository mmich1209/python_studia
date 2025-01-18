# funkcja przyjmuje jako argument ciag znakow i zwraca lizcbe wystapien kazdego znaku w ciagu

def letter_counter(lst):
    dict_counter = {}
    for letter in lst:
        dict_counter[letter] = dict_counter.get(letter, 0) + 1
    return dict_counter


letter_counter("Ala ma kota")
print(letter_counter("Ala ma kota"))


