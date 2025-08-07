import sys

input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = []

for _ in range(N):

    start, end, cost = map(int, input().split())

    if end <= D:  # 고속도로 범위 내일 때만 고려

        shortcuts.append((start, end, cost))

# dp[i]: 0부터 i까지 가는 데 필요한 최소 거리

INF = int(1e9)

dp = [INF] * (D + 1)

dp[0] = 0

for i in range(D + 1):

    # 일반 도로로 1km 가는 경우

    if i + 1 <= D:

        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    # 지름길 이용하는 경우

    for start, end, cost in shortcuts:

        if start == i:

            dp[end] = min(dp[end], dp[start] + cost)

print(dp[D])