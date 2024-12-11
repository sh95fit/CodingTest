import itertools

N, M = map(int, input().split())
numbers = range(1, N + 1)

for seq in itertools.combinations(numbers, M):
    print(*seq)

