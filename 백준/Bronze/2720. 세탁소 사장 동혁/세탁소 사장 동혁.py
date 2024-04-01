# 0.25 0.1 0.05 0.01
# Question
# 3 124 25 194
# Answer
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4

T = int(input())
nlist = [25, 10, 5, 1] 

for _ in range(T):
    clist = []
    C = int(input())  
    for n in nlist:
        clist.append(C // n)
        C = C % n
    print(*clist)
    
    

    
    
    