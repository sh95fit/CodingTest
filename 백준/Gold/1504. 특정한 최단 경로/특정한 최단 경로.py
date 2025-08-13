import sys

import heapq

input = sys.stdin.readline

INF = 10**18

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):

    a, b, c = map(int, input().split())

    graph[a].append((b, c))

    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):

    dist = [INF] * (N + 1)

    dist[start] = 0

    pq = [(0, start)]

    while pq:

        d, u = heapq.heappop(pq)

        if d > dist[u]:

            continue

        for v, w in graph[u]:

            nd = d + w

            if nd < dist[v]:

                dist[v] = nd

                heapq.heappush(pq, (nd, v))

    return dist

d1 = dijkstra(1)

dV1 = dijkstra(v1)

dV2 = dijkstra(v2)

# 두 경로 후보 계산

path1 = d1[v1] + dV1[v2] + dV2[N]   # 1 -> v1 -> v2 -> N

path2 = d1[v2] + dV2[v1] + dV1[N]   # 1 -> v2 -> v1 -> N

ans = min(path1, path2)

print(ans if ans < INF else -1)