from collections import deque

def bfs(grid, visited, start_r, start_c, N, M):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append((start_r, start_c))
    visited[start_r][start_c] = True
    count = 0

    while queue:
        r, c = queue.popleft()
        count += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    return count

def find_largest_food(N, M, K, positions):
    grid = [[0] * M for _ in range(N)]

    for r, c in positions:
        grid[r-1][c-1] = 1

    visited = [[False] * M for _ in range(N)]
    max_size = 0

    for r, c in positions:
        if not visited[r-1][c-1]:
            size = bfs(grid, visited, r-1, c-1, N, M)
            max_size = max(max_size, size)

    return max_size

import sys

input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])
K = int(data[2])
positions = []
index = 3

for _ in range(K):
    r = int(data[index])
    c = int(data[index+1])
    positions.append((r, c))
    index += 2

result = find_largest_food(N, M, K, positions)

print(result)

