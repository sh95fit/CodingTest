import sys
sys.setrecursionlimit(200000)  

def dfs(node):
    for neighbor in graph[node]:
        if parent[neighbor] == -1:  
            parent[neighbor] = node  
            dfs(neighbor)  
            
N = int(input())

graph = [[] for _ in range(N + 1)]  
parent = [-1] * (N + 1)  

for _ in range(N - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

parent[1] = 0
dfs(1)

for i in range(2, N + 1):
    print(parent[i])

