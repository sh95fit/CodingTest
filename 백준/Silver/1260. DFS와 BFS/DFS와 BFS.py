from collections import deque

def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
dfs_result = []
dfs(graph, v, visited_dfs, dfs_result)
print(' '.join(map(str, dfs_result)))

visited_bfs = [False] * (n + 1)
bfs_result = bfs(graph, v, visited_bfs)
print(' '.join(map(str, bfs_result)))
