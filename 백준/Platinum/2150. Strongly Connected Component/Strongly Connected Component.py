import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for _ in range(E):

    a, b = map(int, input().split())

    graph[a].append(b)

id_counter = 1

ids = [0] * (V + 1)

low = [0] * (V + 1)

on_stack = [False] * (V + 1)

stack = []

sccs = []

scc_id = 0

def dfs(u):

    global id_counter

    ids[u] = low[u] = id_counter

    id_counter += 1

    stack.append(u)

    on_stack[u] = True

    for v in graph[u]:

        if ids[v] == 0:

            dfs(v)

            low[u] = min(low[u], low[v])

        elif on_stack[v]:

            low[u] = min(low[u], ids[v])

    if ids[u] == low[u]:

        scc = []

        while True:

            node = stack.pop()

            on_stack[node] = False

            scc.append(node)

            if node == u:

                break

        sccs.append(sorted(scc))  # SCC 내부 오름차순 정렬

for i in range(1, V + 1):

    if ids[i] == 0:

        dfs(i)

# 전체 SCC 오름차순 정렬 (각 SCC의 최소값 기준)

sccs.sort(key=lambda x: x[0])

# 출력

print(len(sccs))

for scc in sccs:

    print(" ".join(map(str, scc)), end=" -1\n")