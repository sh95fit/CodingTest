def draw_star(n, r, c):  
    if n == 1:
        return '*'
       
    size = n // 3
   
    if size <= r % n < 2 * size and size <= c % n < 2 * size:
        return ' '   
    else:
        return draw_star(size, r % size, c % size)

def solve(n):    
    for i in range(n):
        line = ""

        for j in range(n):
            line += draw_star(n, i, j)

        print(line)

N = int(input())

solve(N)

