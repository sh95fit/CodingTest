def count_white_pieces(board):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and board[i][j] == 'F':
                count += 1
    return count

board = []
for _ in range(8):
    board.append(input().strip())

print(count_white_pieces(board))
