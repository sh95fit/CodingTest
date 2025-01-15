import sys
input = sys.stdin.readline

N = int(input().strip())

hlist = list(map(int, input().strip().split()))

swap_count = 0

for _ in range(N):
    for i in range(N-1):
        if hlist[i] > hlist[i+1]:
            hlist[i], hlist[i+1] = hlist[i+1], hlist[i]
            swap_count += 1

    if swap_count == 0:
        break

prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = hlist[i-1] + prefix_sum[i-1]

print(sum(prefix_sum))