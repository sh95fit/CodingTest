from collections import deque

import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().strip())) for _ in range(n)]

dist = [[float('inf')] * n for _ in range(n)]

dist[0][0] = 0

dq = deque()

dq.append((0, 0))

dx = [1, -1, 0, 0]

dy = [0, 0, 1, -1]

while dq:

    x, y = dq.popleft()

    for d in range(4):

        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:

            cost = dist[x][y] + (1 if board[nx][ny] == 0 else 0)

            if cost < dist[nx][ny]:

                dist[nx][ny] = cost

                if board[nx][ny] == 1:

                    dq.appendleft((nx, ny))  # 흰 방은 0비용

                else:

                    dq.append((nx, ny))      # 검은 방은 1비용

print(dist[n-1][n-1])