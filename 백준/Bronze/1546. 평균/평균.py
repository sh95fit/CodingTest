N = int(input())
nlist = list(map(int, input().split(' ')))
M = max(nlist)
res = []

for n in nlist:
    res.append((n / M) * 100)

print(sum(res) / len(res))