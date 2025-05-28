from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1

    return count

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))

print(len(result))        

for count in sorted(result): 
    print(count)