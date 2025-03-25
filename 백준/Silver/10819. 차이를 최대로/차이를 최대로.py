import itertools

N = int(input())  
A = list(map(int, input().split()))  

max_value = 0  

for perm in itertools.permutations(A):
    current_sum = 0

    for i in range(N - 1):
        current_sum += abs(perm[i] - perm[i + 1])  

    max_value = max(max_value, current_sum)  

print(max_value)

