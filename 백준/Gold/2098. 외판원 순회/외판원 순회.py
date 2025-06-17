import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve_tsp():
    N = int(input())
    W = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    dp = [[-1] * (1 << N) for _ in range(N)]

    def dfs(cur, visited):
        if visited == (1 << N) - 1:
            return W[cur][0] if W[cur][0] > 0 else INF

        if dp[cur][visited] != -1:
            return dp[cur][visited]

        min_cost = INF
        for next in range(N):
            if visited & (1 << next) or W[cur][next] == 0:
                continue
            cost = dfs(next, visited | (1 << next)) + W[cur][next]
            min_cost = min(min_cost, cost)

        dp[cur][visited] = min_cost
        return min_cost

    print(dfs(0, 1))

solve_tsp()