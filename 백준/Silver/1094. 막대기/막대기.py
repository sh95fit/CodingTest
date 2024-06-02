def count_sticks(X):

    return bin(X).count('1')

X = int(input())

result = count_sticks(X)

print(result)

