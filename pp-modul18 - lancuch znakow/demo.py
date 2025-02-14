# # # # # # # # # txt = "Ala ma kota"
# # # # # # # # # print(txt)
# # # # # # # # # print(len(txt))
# # # # # # # # # print(len(''))
# # # # # # # #
# # # # # # # #
# # # # # # # # # txt = """asdas
# # # # # # # # # asdasd
# # # # # # # # # adasd"""
# # # # # # # #
# # # # # # # # # print(txt)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # char1 = "a"
# # # # # # # # char2 = " " #spacja
# # # # # # # #
# # # # # # # # print(ord(char1))
# # # # # # # # print(ord(char2))
# # # # # # # # print(ord("ę"))
# # # # # # # # print(hex(ord("ę")))
# # # # # # # # print("\u0119")
# # # # # # # #
# # # # # # # # # znak może być zakodowany za pomocą 1, 2, 3 lub 4 bajtów
# # # # # # # #
# # # # # # # # c = "a"
# # # # # # # # print(c, ord(c), hex(ord(c)), c.encode())
# # # # # # #
# # # # # # # # znak euro
# # # # # # #
# # # # # # # c = "\u20AC"
# # # # # # # print(c, ord(c), hex(ord(c)), c.encode())
# # # # # #
# # # # # # print(chr(97))
# # # # # # print(chr(945))
# # # # # # print("a" == chr(ord("a")))
# # # # #
# # # # #      0123456789
# # # # txt = "Ala ma kota."
# # # # #
# # # # # for c in txt:
# # # # #     print(c, end=" ")
# # # # #
# # # # # print()
# # # # # for i in range(len(txt)):
# # # # #     print(i, txt[i])
# # # #
# # # #
# # # # print(txt[4:6])
# # # # print(txt[7:])
# # # # print(txt[-1:])
# # # # print(txt[2::3])
# # #
# # #
# # # print(ord("a"))
# # # print(ord("z"))
# # #
# # # for i in range(ord('a'), ord('z')+1):
# # #     print(chr(i), end="")
# #
# #
# # alpahbet = ""
# # for i in range(ord('a'), ord('z') + 1):
# #     alpahbet = alpahbet + chr(i)
# # print(alpahbet)
# #
# # print("a" in alpahbet)
# # print("A" in alpahbet)
# # print("A" not in alpahbet)
#
#
# print(min([1, 2, 3]))
# print(max("abcABC"))
# print(min("abcABC"))
# print(min("Ala ma kota."))
# print(max("Ala ma kota."))


alphabet = ""
for i in range(ord('a'), ord('z')+1):
    alphabet = alphabet + chr(i)

print(alphabet)
# print("aaabbbccc".index("c"))
#

print("Ala ma kota.".count("a"))
print([1, 2, 3].count(1))