import sys

input = sys.stdin.read

data = input().splitlines()
N, M = map(int, data[0].split())
arr = []

for i in range(1, N + 1):
    arr.append(list(map(int, data[i].split())))

prefix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix[i][j] = arr[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

result = []

for i in range(N + 1, N + M + 1):
    x1, y1, x2, y2 = map(int, data[i].split())
    sum_val = prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]
    result.append(str(sum_val))

sys.stdout.write("\n".join(result) + "\n")

