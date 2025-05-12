import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.read

def bfs(N, graph, R):
    visited = [0] * (N + 1)  
    order = 1  
    queue = deque([R])
    visited[R] = order

    while queue:
        u = queue.popleft()

        for v in sorted(graph[u], reverse=True):  
            if visited[v] == 0:
                order += 1
                visited[v] = order
                queue.append(v)

    return visited[1:]  

def main():
    data = input().split()
    N, M, R = map(int, data[:3])
    edges = list(map(int, data[3:]))
    graph = [[] for _ in range(N + 1)]

    for i in range(0, 2 * M, 2):
        u, v = edges[i], edges[i + 1]
        graph[u].append(v)
        graph[v].append(u)

    result = bfs(N, graph, R)

    print('\n'.join(map(str, result)))

main()