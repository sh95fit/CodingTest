def solve():
    S, K = map(int, input().split())
       
    quotient = S // K
    remainder = S % K         
    result = 1

    for i in range(K):
        if i < remainder:
            result *= (quotient + 1)  
        else:
            result *= quotient  
    
    print(result)

solve()

