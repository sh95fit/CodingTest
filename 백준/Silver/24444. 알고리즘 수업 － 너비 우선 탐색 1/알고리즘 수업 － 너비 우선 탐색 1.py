import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_order = [0] * (N + 1) 
cnt = 1  

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

def bfs(start):
    global cnt
    queue = deque([start])
    visited_order[start] = cnt

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited_order[neighbor] == 0:
                cnt += 1
                visited_order[neighbor] = cnt
                queue.append(neighbor)

bfs(R)

for i in range(1, N + 1):
    print(visited_order[i])
