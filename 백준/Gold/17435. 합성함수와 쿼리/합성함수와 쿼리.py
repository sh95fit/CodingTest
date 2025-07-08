import sys
input = sys.stdin.readline

sys.setrecursionlimit(1 << 25)

m = int(input())
f = list(map(int, input().split()))
Q = int(input())

LOG = 20  
table = [[0] * (m + 1) for _ in range(LOG)]

for i in range(1, m + 1):
    table[0][i] = f[i - 1]

for k in range(1, LOG):
    for x in range(1, m + 1):
        table[k][x] = table[k - 1][table[k - 1][x]]

for _ in range(Q):
    n, x = map(int, input().split())

    for k in range(LOG):
        if n & (1 << k):
            x = table[k][x]

    print(x)