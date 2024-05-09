N = int(input())
nlist = []
    
for _ in range(N):
    num = int(input())
    
    if num == 0 :
        nlist.pop()
    else :
        nlist.append(num)

print(sum(nlist))