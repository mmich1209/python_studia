#tworzymy plansze do gry w szachy
#
# chess_row = ["--" for i in range(8) ]
# print(chess_row)
#
# chess_board = [chess_row[:] for _ in range(8)]
# print(chess_board)

chessboard = [["--" for i in range(8)] for _ in range(8)]


print(chessboard)

WHITE_POWN = "BP"
BLACK_POWN = "CP"

chessboard[3][4] = WHITE_POWN
chessboard[2][7] = BLACK_POWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()

