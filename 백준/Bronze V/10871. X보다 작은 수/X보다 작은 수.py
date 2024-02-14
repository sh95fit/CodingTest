T, B = list(map(int, input().split(" ")))
nlist = list(map(int, input().split(" ")))
res = ""

for i in range(T) :
    if nlist[i] < B :
        res += f"{nlist[i]} "

print(res.strip())