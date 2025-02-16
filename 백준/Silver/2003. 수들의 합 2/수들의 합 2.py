def find_subarrays_with_sum(N, M, A):
    start = 0
    end = 0
    current_sum = 0
    count = 0

    while end < N:
        current_sum += A[end]  
        end += 1
               
        while current_sum > M and start < end:
            current_sum -= A[start]
            start += 1
                
        if current_sum == M:
            count += 1
    
    return count

N, M = map(int, input().split())
A = list(map(int, input().split()))

print(find_subarrays_with_sum(N, M, A))

