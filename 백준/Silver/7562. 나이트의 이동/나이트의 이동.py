from collections import deque

directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
              (-1, -2), (-1, 2), (1, -2), (1, 2)]

def bfs(l, start, end):   
    queue = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    distance = 0
    
    while queue:
        size = len(queue)

        for _ in range(size):
            x, y = queue.popleft()
                       
            if (x, y) == end:
                return distance
                    
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
               
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
              
        distance += 1

    return -1  

def main():
    t = int(input())  

    for _ in range(t):
        l = int(input())  
        start = tuple(map(int, input().split()))  
        end = tuple(map(int, input().split()))  
              
        if start == end:
            print(0)
        else:
            print(bfs(l, start, end))  

if __name__ == "__main__":
    main()

