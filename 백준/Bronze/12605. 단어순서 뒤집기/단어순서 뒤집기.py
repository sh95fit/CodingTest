import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1, N+1):
    slist = input().split()
    slist.reverse()
    
    print(f"Case #{i}: {' '.join(slist)}")