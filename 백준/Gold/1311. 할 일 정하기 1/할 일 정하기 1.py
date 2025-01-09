def solve():
    import sys

    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    D = [list(map(int, data[i * N + 1:(i + 1) * N + 1])) for i in range(N)]
    
    dp = [float('inf')] * (1 << N)
    dp[0] = 0
    
    for state in range(1 << N):
        person = bin(state).count('1')  # 현재까지 할당된 사람 수

        if person >= N:
            continue

        for job in range(N):
            if not (state & (1 << job)):  
                next_state = state | (1 << job)
                dp[next_state] = min(dp[next_state], dp[state] + D[person][job])
    
    print(dp[(1 << N) - 1])

solve()

