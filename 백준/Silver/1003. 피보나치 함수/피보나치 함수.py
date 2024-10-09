def fibonacci_count(n, counts):
    if n in counts:
        return counts[n]
    
    if n == 0:
        counts[n] = (1, 0)  
    elif n == 1:
        counts[n] = (0, 1)  
    else:
        zero_count_n1, one_count_n1 = fibonacci_count(n - 1, counts)
        zero_count_n2, one_count_n2 = fibonacci_count(n - 2, counts)
        counts[n] = (zero_count_n1 + zero_count_n2, one_count_n1 + one_count_n2)
   
    return counts[n]

T = int(input().strip())
results = []
counts = {}

for _ in range(T):
    N = int(input().strip())
    results.append(fibonacci_count(N, counts))

for zero_count, one_count in results:
    print(zero_count, one_count)

