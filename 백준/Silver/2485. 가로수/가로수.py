import sys

import math

from functools import reduce

# 입력 받기

input = sys.stdin.read

data = input().split()

N = int(data[0])

positions = list(map(int, data[1:]))

# 모든 간격 계산

distances = [positions[i+1] - positions[i] for i in range(N-1)]

# 모든 간격의 최대공약수 계산

gcd_all = reduce(math.gcd, distances)

# 각 간격이 gcd의 배수가 되도록 필요한 가로수의 수 계산

total_trees_needed = 0

for distance in distances:

    total_trees_needed += (distance // gcd_all) - 1

print(total_trees_needed)

