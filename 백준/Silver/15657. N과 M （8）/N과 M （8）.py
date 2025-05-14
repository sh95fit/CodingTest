from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

result = combinations_with_replacement(nums, M)

for seq in result:
    print(' '.join(map(str, seq)))