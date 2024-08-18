def find_truthful_statements(n, statements):
    for x in range(n, -1, -1):
        if statements.count(x) == x:
            return x

    return -1

n = int(input())
statements = list(map(int, input().split()))

result = find_truthful_statements(n, statements)
print(result)

