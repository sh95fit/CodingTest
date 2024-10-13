import sys
from collections import defaultdict

sys_input = sys.stdin.read
input = sys.stdin.readline

class Tree:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.parent = [0] * (n + 1)
        self.depth = [0] * (n + 1)
        self.distance = [0] * (n + 1)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dfs(self, node, par, dep):
        self.parent[node] = par
        self.depth[node] = dep

        for neighbor, weight in self.graph[node]:
            if neighbor != par:
                self.distance[neighbor] = self.distance[node] + weight
                self.dfs(neighbor, node, dep + 1)

    def lca(self, u, v):
        while u != v:
            if self.depth[u] > self.depth[v]:
                u = self.parent[u]
            else:
                v = self.parent[v]

        return u

    def distance_between_nodes(self, u, v):
        lca_node = self.lca(u, v)

        return self.distance[u] + self.distance[v] - 2 * self.distance[lca_node]

N, M = map(int, input().strip().split())
tree = Tree(N)

for _ in range(N - 1):
    u, v, w = map(int, input().strip().split())
    tree.add_edge(u, v, w)

tree.dfs(1, -1, 0)
results = []

for _ in range(M):
    u, v = map(int, input().strip().split())
    results.append(tree.distance_between_nodes(u, v))

print("\n".join(map(str, results)))

