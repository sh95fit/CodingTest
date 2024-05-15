import sys

N = int(sys.stdin.readline())
nlist = []

for _ in range(N):
    n = int(sys.stdin.readline())
    nlist.append(n)
    
nlist.sort()

for num in nlist:
    print(num)
