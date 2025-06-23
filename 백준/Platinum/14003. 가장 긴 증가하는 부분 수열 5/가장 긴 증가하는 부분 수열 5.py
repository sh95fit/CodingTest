import sys
import bisect

input = sys.stdin.read

data = input().split()
n = int(data[0])
A = list(map(int, data[1:]))

lis = []
pos = [0] * n

for i in range(n):
    num = A[i]
    idx = bisect.bisect_left(lis, num)

    if idx == len(lis):
        lis.append(num)

    else:
        lis[idx] = num

    pos[i] = idx

length = len(lis)
print(length)

result = []
cur_idx = length - 1

for i in range(n - 1, -1, -1):
    if pos[i] == cur_idx:
        result.append(A[i])
        cur_idx -= 1

    if cur_idx < 0:
        break

print(' '.join(map(str, reversed(result))))