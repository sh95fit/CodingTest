from collections import deque

def shortest_path_with_break(N, M, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0, 1))  
    visited[0][0][0] = True

    while queue:
        x, y, broken, dist = queue.popleft()

        if x == N - 1 and y == M - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, broken, dist + 1))

                elif graph[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

print(shortest_path_with_break(N, M, graph))
