import heapq

def trap_rain_water(grid):
    if not grid or not grid[0]:
        return 0

    N = len(grid)
    M = len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    min_heap = []
    visited = [[False] * M for _ in range(N)]

    for r in range(N):
        heapq.heappush(min_heap, (grid[r][0], r, 0))
        heapq.heappush(min_heap, (grid[r][M-1], r, M-1))

        visited[r][0] = True
        visited[r][M-1] = True

    for c in range(M):
        heapq.heappush(min_heap, (grid[0][c], 0, c))
        heapq.heappush(min_heap, (grid[N-1][c], N-1, c))
        visited[0][c] = True
        visited[N-1][c] = True

    water_trapped = 0
    max_height = 0

    while min_heap:
        height, r, c = heapq.heappop(min_heap)
        max_height = max(max_height, height)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                water_trapped += max(0, max_height - grid[nr][nc])
                heapq.heappush(min_heap, (max(max_height, grid[nr][nc]), nr, nc))

    return water_trapped

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

print(trap_rain_water(grid))

