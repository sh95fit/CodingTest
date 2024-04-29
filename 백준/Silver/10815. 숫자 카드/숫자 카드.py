N = int(input())
nlist = set(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))

res = []

for m in mlist:
    if m in nlist :
        res.append(1)
    else :
        res.append(0)

print(*res)


