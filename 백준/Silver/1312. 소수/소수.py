def get_decimal_place(A, B, N):   
    remainder = A % B
        
    for _ in range(N):
        remainder *= 10  
        decimal_digit = remainder // B  
        remainder = remainder % B 
    
    return decimal_digit

A, B, N = map(int, input().split())

print(get_decimal_place(A, B, N))

