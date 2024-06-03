def min_difference(A, B):
    len_A = len(A)
    len_B = len(B)
    min_diff = float('inf')
    
    for i in range(len_B - len_A + 1):
        diff = 0

        for j in range(len_A):
            if A[j] != B[i + j]:
                diff += 1

        min_diff = min(min_diff, diff)
    
    return min_diff

A, B = input().split()
print(min_difference(A, B))
