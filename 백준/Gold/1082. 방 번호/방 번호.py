def solve():
    N = int(input())  
    P = list(map(int, input().split()))  
    M = int(input())  
   
    min_price = min(P)
    min_digit = P.index(min_price)
   
    min_non_zero_price = float('inf')
    min_non_zero_digit = -1

    for i in range(1, N):
        if P[i] < min_non_zero_price:
            min_non_zero_price = P[i]
            min_non_zero_digit = i
   
    if M < min_non_zero_price:
        print(0)

        return
   
    result = [min_non_zero_digit]
    M -= min_non_zero_price   
    length = M // min_price
    result += [min_digit] * length
    M -= min_price * length
   
    for i in range(len(result)):
        for d in range(N-1, -1, -1):
            if i == 0 and d == 0: 
                continue

            cost = P[d] - P[result[i]]

            if M >= cost:
                result[i] = d
                M -= cost
                break

    print(''.join(map(str, result)))

solve()

