def find_worms(M, N, cabbages):
    from collections import deque
   
    field = [[0] * N for _ in range(M)]

    for x, y in cabbages:
        field[x][y] = 1

    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        field[start_x][start_y] = 0  # Mark as visited

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1:
                    field[nx][ny] = 0  
                    queue.append((nx, ny))

    worm_count = 0

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                bfs(i, j)
                worm_count += 1 

    return worm_count

import sys

input = sys.stdin.read

data = input().split()
index = 0

T = int(data[index])
index += 1
results = []

for _ in range(T):
    M = int(data[index])
    N = int(data[index + 1])
    K = int(data[index + 2])

    index += 3  
    cabbages = []

    for _ in range(K):
        x = int(data[index])
        y = int(data[index + 1])

        cabbages.append((x, y))
        index += 2

    result = find_worms(M, N, cabbages)
    results.append(result)

for result in results:
    print(result)

