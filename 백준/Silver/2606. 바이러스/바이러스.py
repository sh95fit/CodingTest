def dfs(graph, visited, node):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

n = int(input())  
m = int(input()) 
graph = [[] for _ in range(n + 1)]  # 컴퓨터 번호는 1번부터 시작하므로 n+1 크기로 초기화

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(graph, visited, 1)

print(visited.count(True) - 1)

