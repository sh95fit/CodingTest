from collections import defaultdict

def count_divisible_subarrays(N, M, A):   
    remainder_count = defaultdict(int)       
    remainder_count[0] = 1    
    prefix_sum = 0
    result = 0
    
    for num in A:       
        prefix_sum += num
        remainder = prefix_sum % M
               
        if remainder < 0:
            remainder += M
               
        result += remainder_count[remainder]              
        remainder_count[remainder] += 1
    
    return result

N, M = map(int, input().split())
A = list(map(int, input().split()))

print(count_divisible_subarrays(N, M, A))

