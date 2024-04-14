N = int(input())
nlist = []

for _ in range(N) :
    nlist.append(int(input()))
   

nlist = sorted(nlist)
        
for i in range(len(nlist)) :
    print(nlist[i])