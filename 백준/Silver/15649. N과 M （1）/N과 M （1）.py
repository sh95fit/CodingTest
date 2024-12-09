import itertools

N, M = map(int, input().split())
numbers = range(1, N + 1)
permutations = itertools.permutations(numbers, M)

for p in permutations:
    print(" ".join(map(str, p)))

