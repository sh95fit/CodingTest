def flip_3x3(matrix, x, y):
    for i in range(3):
        for j in range(3):
            matrix[x + i][y + j] = 1 - matrix[x + i][y + j]

def min_operations_to_transform(N, M, A, B):
    if N < 3 or M < 3:
        return -1 if A != B else 0 

    count = 0

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip_3x3(A, i, j)
                count += 1

    if A == B:
        return count
    else:
        return -1

import sys

input = sys.stdin.read

data = input().split()

N = int(data[0])
M = int(data[1])

A = []
B = []
index = 2

for i in range(N):
    A.append([int(x) for x in data[index]])
    index += 1

for i in range(N):
    B.append([int(x) for x in data[index]])
    index += 1

print(min_operations_to_transform(N, M, A, B))

