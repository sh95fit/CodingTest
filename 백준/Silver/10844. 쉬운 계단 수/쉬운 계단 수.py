MOD = 1000000000

def count_stair_numbers(N):
    dp = [[0] * 10 for _ in range(N+1)]
   
    for i in range(1, 10):
        dp[1][i] = 1
   
    for i in range(2, N+1):
        for j in range(10):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]

            if j < 9:
                dp[i][j] += dp[i-1][j+1]

            dp[i][j] %= MOD
  
    return sum(dp[N]) % MOD

N = int(input())
print(count_stair_numbers(N))