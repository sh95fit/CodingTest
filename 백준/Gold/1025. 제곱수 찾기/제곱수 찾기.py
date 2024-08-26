import math

def is_perfect_square(x):
    root = int(math.isqrt(x))

    return root * root == x

def solve(n, m, board):
    max_square = -1

    for i in range(n):
        for j in range(m):
            for dr in range(-n, n):
                for dc in range(-m, m):
                    if dr == 0 and dc == 0:
                        continue
                 
                    number = ''
                    r, c = i, j

                    while 0 <= r < n and 0 <= c < m:
                        number += board[r][c]
                        num_int = int(number)

                        if is_perfect_square(num_int):
                            max_square = max(max_square, num_int)

                        r += dr
                        c += dc

    return max_square

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

result = solve(n, m, board)
print(result)

