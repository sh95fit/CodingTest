N = int(input())
A = set(map(int, input().split()))
M = int(input())
queries = map(int, input().split())

for query in queries:
    if query in A:
        print(1)

    else:
        print(0)

