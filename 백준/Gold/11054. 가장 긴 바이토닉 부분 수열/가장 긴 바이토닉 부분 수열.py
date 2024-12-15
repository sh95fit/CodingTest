def longest_bitonic_subsequence(N, A):   
    lis = [1] * N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                lis[i] = max(lis[i], lis[j] + 1)
       
    lds = [1] * N

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if A[i] > A[j]:
                lds[i] = max(lds[i], lds[j] + 1)
       
    max_len = 0

    for i in range(N):
        max_len = max(max_len, lis[i] + lds[i] - 1)
    
    return max_len

N = int(input())  
A = list(map(int, input().split()))  

print(longest_bitonic_subsequence(N, A))

