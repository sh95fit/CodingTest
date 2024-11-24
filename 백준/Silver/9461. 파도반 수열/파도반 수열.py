def calculate_padoban(n):   
    pado = [0] * (n + 1)       
    pado[1] = 1
    pado[2] = 1
    pado[3] = 1
       
    for i in range(4, n + 1):
        pado[i] = pado[i - 2] + pado[i - 3]
    
    return pado

T = int(input())

max_n = 100  
pado = calculate_padoban(max_n)

for _ in range(T):
    N = int(input())
    print(pado[N])

