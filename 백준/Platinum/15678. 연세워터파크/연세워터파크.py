from collections import deque

import sys

input = sys.stdin.readline

N, D = map(int, input().split())
K = list(map(int, input().split()))

dp = [0] * N
dp[0] = K[0]

answer = dp[0]

dq = deque()
dq.append(0)

for i in range(1, N):   
    while dq and dq[0] < i - D:
        dq.popleft()
   
    dp[i] = K[i]

    if dq:
        dp[i] = max(dp[i], K[i] + dp[dq[0]])

    answer = max(answer, dp[i])
   
    while dq and dp[dq[-1]] <= dp[i]:
        dq.pop()

    dq.append(i)

print(answer)