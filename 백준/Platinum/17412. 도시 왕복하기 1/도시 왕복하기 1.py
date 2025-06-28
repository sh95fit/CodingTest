import sys
from collections import deque

INF = 10**9

input = sys.stdin.readline

class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, c):        
        self.adj[u].append([v, c, len(self.adj[v])])      
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def bfs(self, s, t, level):
        q = deque([s])
        level[:] = [-1] * self.n
        level[s] = 0

        while q:
            u = q.popleft()

            for v, cap, _ in self.adj[u]:
                if cap and level[v] == -1:
                    level[v] = level[u] + 1
                    q.append(v)

        return level[t] != -1

    def dfs(self, u, t, f, level, it):
        if u == t:
            return f

        for i in range(it[u], len(self.adj[u])):
            it[u] = i
            v, cap, rev = self.adj[u][i]

            if cap and level[u] + 1 == level[v]:
                pushed = self.dfs(v, t, min(f, cap), level, it)

                if pushed:                   
                    self.adj[u][i][1] -= pushed
                    self.adj[v][rev][1] += pushed

                    return pushed

        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1]*self.n

        while self.bfs(s, t, level):
            it = [0]*self.n

            while True:
                f = self.dfs(s, t, INF, level, it)

                if not f:
                    break

                flow += f

        return flow

def main():
    N, P = map(int, input().split())
    dinic = Dinic(N + 1)         

    for _ in range(P):
        u, v = map(int, input().split())
        dinic.add_edge(u, v, 1)  

    ans = dinic.max_flow(1, 2)

    print(ans)

if __name__ == "__main__":
    main()