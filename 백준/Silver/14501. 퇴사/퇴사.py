N = int(input())

T = []
P = []

for _ in range(N):
    Ti, Pi = map(int, input().split())

    T.append(Ti)
    P.append(Pi)

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):   
    end_day = i + T[i]
       
    if end_day <= N:       
        dp[i] = max(dp[i], P[i] + dp[end_day])
       
    dp[i] = max(dp[i], dp[i + 1])

print(dp[0])

