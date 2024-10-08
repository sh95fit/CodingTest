def find_consecutive_sum(N, L):
    for k in range(L, 101):      
        sum_of_first_k_minus_1 = k * (k - 1) // 2
               
        if N >= sum_of_first_k_minus_1:
            remainder = N - sum_of_first_k_minus_1

            if remainder % k == 0:
                x = remainder // k               
                sequence = [x + i for i in range(k)]

                print(" ".join(map(str, sequence)))

                return
    
    print(-1)

N, L = map(int, input().split())

find_consecutive_sum(N, L)

