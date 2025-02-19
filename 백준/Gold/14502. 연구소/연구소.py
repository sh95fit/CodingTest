from collections import deque
import itertools

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(lab, N, M):   
    visited = [[False] * M for _ in range(N)]
    queue = deque()
       
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:  
                queue.append((i, j))
                visited[i][j] = True
       
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and lab[nx][ny] == 0:
                visited[nx][ny] = True
                lab[nx][ny] = 2  
                queue.append((nx, ny))
       
    safe_area = 0

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                safe_area += 1

    return safe_area

def solve():
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]       
    empty_spaces = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                empty_spaces.append((i, j))
    
    max_safe_area = 0
       
    for walls in itertools.combinations(empty_spaces, 3):       
        new_lab = [row[:] for row in lab]

        for wx, wy in walls:
            new_lab[wx][wy] = 1  
               
        safe_area = bfs(new_lab, N, M)                
        max_safe_area = max(max_safe_area, safe_area)
    
    print(max_safe_area)

if __name__ == "__main__":
    solve()

