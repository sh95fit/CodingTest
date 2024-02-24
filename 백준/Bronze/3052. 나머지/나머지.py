nlist = []

for _ in range(10):
    nlist.append(int(input())%42)
 
nlist = list(set(nlist))

print(len(nlist))

