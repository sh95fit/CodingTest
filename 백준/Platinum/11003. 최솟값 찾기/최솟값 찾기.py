from collections import deque
import sys

input = sys.stdin.readline  

N, L = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
result = []

for i in range(N):   
    while dq and dq[0] < i - L + 1:
        dq.popleft()
  
    while dq and A[dq[-1]] > A[i]:
        dq.pop()
   
    dq.append(i)
    
    result.append(str(A[dq[0]]))

print(' '.join(result))