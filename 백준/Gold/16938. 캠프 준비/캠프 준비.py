N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
count = 0

for bit in range(1, 1 << N):
    selected = []

    for i in range(N):
        if bit & (1 << i):  
            selected.append(A[i])

    if len(selected) >= 2:
        total = sum(selected)
        diff = max(selected) - min(selected)

        if L <= total <= R and diff >= X:
            count += 1

print(count)