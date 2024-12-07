# Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
# • stwórz wirtualną szachownicę,
# • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
# • zaprezentuj użytkownikowi stan wirtualnej szachownicy

# tworzymy plansze do gry w szachy

#chess_row = ["--", "--", "--", "--", "--", "--", "--", "--"]
"""
chess_row = ["--" for _ in range(8)]
print(chess_row)


chessboard = [chess_row[:] for _ in range(8)]
print(chessboard)
"""
import random

chessboard = [["--" for _ in range(8)] for _ in range(8)]
print(chessboard)

WHITE_POWN = "BP"
BLACK_POWN = "CP"

chessboard[3][4] = WHITE_POWN
chessboard[2][7] = BLACK_POWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()
