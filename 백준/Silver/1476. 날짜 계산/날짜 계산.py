def solve(E, S, M):
    year = 1

    while True:
        if (year - 1) % 15 + 1 == E and (year - 1) % 28 + 1 == S and (year - 1) % 19 + 1 == M:
            return year

        year += 1

E, S, M = map(int, input().split())

print(solve(E, S, M))

