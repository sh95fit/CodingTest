import sys

from collections import deque

INF = 10 ** 9

input = sys.stdin.readline

def hopcroft_karp(g, n_left, n_right):

    """g[u] = list of v (0-based) that u can match to"""

    pair_u = [-1] * n_left

    pair_v = [-1] * n_right

    dist   = [0]  * n_left

    def bfs():

        q = deque()

        for u in range(n_left):

            if pair_u[u] == -1:

                dist[u] = 0

                q.append(u)

            else:

                dist[u] = INF

        found = False

        while q:

            u = q.popleft()

            for v in g[u]:

                pu = pair_v[v]

                if pu != -1 and dist[pu] == INF:

                    dist[pu] = dist[u] + 1

                    q.append(pu)

                elif pu == -1:

                    found = True

        return found

    def dfs(u):

        for v in g[u]:

            pu = pair_v[v]

            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):

                pair_u[u] = v

                pair_v[v] = u

                return True

        dist[u] = INF

        return False

    matching = 0

    while bfs():

        for u in range(n_left):

            if pair_u[u] == -1 and dfs(u):

                matching += 1

    return matching

def smaller(a, b):

    """True if a[t] < b[t] for all t"""

    return all(x < y for x, y in zip(a, b))

T = int(input())

for case in range(1, T + 1):

    n, k = map(int, input().split())

    stocks = [list(map(int, input().split())) for _ in range(n)]

    graph = [[] for _ in range(n)]

    for i in range(n):

        for j in range(n):

            if i != j and smaller(stocks[i], stocks[j]):

                graph[i].append(j)

    max_match = hopcroft_karp(graph, n, n)

    ans = n - max_match

    print(f"Case #{case}: {ans}")