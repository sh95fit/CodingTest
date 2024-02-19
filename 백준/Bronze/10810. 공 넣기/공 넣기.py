N,M = list(map(int, input().split(' ')))

res = [0]*N

for _ in range(M) :
    i,j,k = list(map(int,input().split(' ')))
    for t in range(i-1,j):
        res[t] = k
print(*res)