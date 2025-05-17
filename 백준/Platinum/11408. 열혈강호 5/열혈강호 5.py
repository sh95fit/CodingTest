import heapq
from collections import deque

INF = int(1e9)

class Edge:
    def __init__(self, to, rev, capacity, cost):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.cost = cost

class MinCostMaxFlow:
    def __init__(self, N):
        self.N = N
        self.graph = [[] for _ in range(N)]

    def add(self, fr, to, cap, cost):
        forward = Edge(to, len(self.graph[to]), cap, cost)
        backward = Edge(fr, len(self.graph[fr]), 0, -cost)

        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def flow(self, s, t):
        N = self.N
        prevv = [0] * N
        preve = [0] * N
        res = 0
        flow = 0
        h = [0] * N  

        while True:
            dist = [INF] * N
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heapq.heappop(que)

                if dist[v] < c:
                    continue

                for i, e in enumerate(self.graph[v]):
                    if e.capacity > 0 and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to] = v
                        preve[e.to] = i
                        heapq.heappush(que, (dist[e.to], e.to))

            if dist[t] == INF:
                break

            for v in range(N):
                h[v] += dist[v]

            d = INF
            v = t

            while v != s:
                d = min(d, self.graph[prevv[v]][preve[v]].capacity)
                v = prevv[v]

            flow += d
            res += d * h[t]
            v = t

            while v != s:
                e = self.graph[prevv[v]][preve[v]]
                e.capacity -= d
                self.graph[v][e.rev].capacity += d
                v = prevv[v]

        return flow, res

N, M = map(int, input().split())
S = N + M
T = N + M + 1
mcmf = MinCostMaxFlow(N + M + 2)

for i in range(N):
    data = list(map(int, input().split()))
    k = data[0]

    for j in range(k):
        job = data[1 + j * 2] - 1
        cost = data[2 + j * 2]
        mcmf.add(i, N + job, 1, cost)

for i in range(N):
    mcmf.add(S, i, 1, 0)

for j in range(M):
    mcmf.add(N + j, T, 1, 0)

count, total_cost = mcmf.flow(S, T)

print(count)
print(total_cost)