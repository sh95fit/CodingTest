def mars_exploration():
    import sys

    input = sys.stdin.read
    data = input().strip().split()
    
    N, M = int(data[0]), int(data[1])
    grid = [list(map(int, data[i * M + 2:(i + 1) * M + 2])) for i in range(N)]
       
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = grid[0][0]
       
    for j in range(1, M):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
       
    for i in range(1, N):       
        left = [0] * M
        left[0] = dp[i - 1][0] + grid[i][0]

        for j in range(1, M):
            left[j] = max(left[j - 1], dp[i - 1][j]) + grid[i][j]
               
        right = [0] * M
        right[M - 1] = dp[i - 1][M - 1] + grid[i][M - 1]

        for j in range(M - 2, -1, -1):
            right[j] = max(right[j + 1], dp[i - 1][j]) + grid[i][j]
               
        for j in range(M):
            dp[i][j] = max(left[j], right[j])
       
    print(dp[N - 1][M - 1])

mars_exploration()

