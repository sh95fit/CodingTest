import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

freq = Counter(A)
result = [-1] * N
stack = []

for i in range(N - 1, -1, -1):   
    while stack and freq[A[i]] >= freq[stack[-1]]:
        stack.pop()
      
    if stack:
        result[i] = stack[-1]

    stack.append(A[i])

print(' '.join(map(str, result)))