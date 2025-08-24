import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

semester = [1] * (N+1)   # 기본값: 선수 과목 없으면 1학기

for _ in range(M):

    A, B = map(int, input().split())

    graph[A].append(B)

    indegree[B] += 1

q = deque()

# 선수 과목 없는 과목들 큐에 넣기

for i in range(1, N+1):

    if indegree[i] == 0:

        q.append(i)

while q:

    u = q.popleft()

    for v in graph[u]:

        # u를 들었으니 v는 u 학기 + 1 이상 가능

        semester[v] = max(semester[v], semester[u] + 1)

        indegree[v] -= 1

        if indegree[v] == 0:

            q.append(v)

print(" ".join(map(str, semester[1:])))