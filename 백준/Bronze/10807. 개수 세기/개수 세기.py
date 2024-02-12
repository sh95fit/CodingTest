T=int(input())
nlist=list(map(int,input().split(' ')))
n=int(input())
res=0

for i in range(T):
  if n == nlist[i] :
        res += 1

print(res)