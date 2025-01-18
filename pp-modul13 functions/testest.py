# # def divisible_by_ten(nums):
# #     counter = 0
# #     for number in nums:
# #         if (number % 10 == 0):
# #             counter += 1
# #     return counter
# #
# # print(divisible_by_ten([20,25,30,35,40]))
# # #loop through elements of list
#
#
# def larger_sum(lst1, lst2):
#     sum_lst1 = sum(lst1)
#     sum_lst2 = sum(lst2)
#     if sum_lst1 > sum_lst2:
#         return lst1
#     else:
#         return lst2
#
# print(larger_sum([1,9,5], [20,3,7]))
#
#
#
#
# def delete_starting_evens(my_list):
#     while (len(my_list) > 0 and my_list[0] % 2 == 0):
#        my_list = my_list[1:]
#     return my_list
#
# Wytlumacz mi to:
# my_list = my_list[1:]
# ChatGPT said:
# ChatGPT
# W instrukcji my_list = my_list[1:] dzieje się następujące:
#
# Co oznacza my_list[1:]?
# my_list[1:] tworzy nową listę, która zawiera wszystkie elementy z my_list od indeksu 1 do końca listy.
# Innymi słowy, usuwa pierwszy element listy (my_list[0]) i zwraca resztę.
# Przykład:
#
# python
# Copy code
# my_list = [2, 4, 6, 8]
# print(my_list[1:])  # Wynik: [4, 6, 8]
# Co oznacza przypisanie my_list = my_list[1:]?
# Po wykonaniu tej operacji, zmienna my_list zostaje zaktualizowana i teraz przechowuje listę bez pierwszego elementu.
# Oryginalna lista zostaje "skrócona" o pierwszy element.
# Przykład:
#
# python
# Copy code
# my_list = [2, 4, 6, 8]
# my_list = my_list[1:]  # Zaktualizowana lista: [4, 6, 8]
# W kontekście funkcji:
# Funkcja delete_starting_evens działa w pętli while, która:
#
# Sprawdza, czy lista nie jest pusta (len(my_list) > 0).
# Sprawdza, czy pierwszy element listy (my_list[0]) jest liczbą parzystą (% 2 == 0).
# Jeśli oba warunki są spełnione:
#
# Pierwszy element (parzysty) zostaje usunięty za pomocą my_list = my_list[1:].
# Pętla kończy się, gdy:
#
# Lista jest pusta.
# Pierwszy element listy nie jest parzysty.
# Przykład działania:
# python
# Copy code
# my_list = [2, 4, 6, 7, 8]
# result = delete_starting_evens(my_list)
# print(result)  # Wynik: [7, 8]
# Krok po kroku:
#
# my_list = [2, 4, 6, 7, 8] → Pierwszy element 2 (parzysty) zostaje usunięty.
# my_list = [4, 6, 7, 8] → Pierwszy element 4 (parzysty) zostaje usunięty.
# my_list = [6, 7, 8] → Pierwszy element 6 (parzysty) zostaje usunięty.
# my_list = [7, 8] → Pierwszy element 7 (nieparzysty), pętla się kończy.
# Funkcja zwraca [7, 8].
#
# Podsumowanie:
# my_list[1:] pozwala usunąć pierwszy element listy.
# Operacja jest powtarzana w pętli, aż spełniony zostanie warunek zatrzymania (brak parzystych liczb na początku listy).
#
#
#
#
#
