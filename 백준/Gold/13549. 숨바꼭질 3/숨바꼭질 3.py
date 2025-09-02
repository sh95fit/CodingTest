from collections import deque

def hide_and_seek(N, K):

    MAX = 100000

    dist = [-1] * (MAX + 1)

    dq = deque()

    

    dq.append(N)

    dist[N] = 0

    

    while dq:

        cur = dq.popleft()

        

        if cur == K:

            return dist[cur]

        

        # 순간이동 (0초)

        if 0 <= cur * 2 <= MAX and dist[cur * 2] == -1:

            dist[cur * 2] = dist[cur]

            dq.appendleft(cur * 2)

        

        # 걷기 (-1)

        if 0 <= cur - 1 <= MAX and dist[cur - 1] == -1:

            dist[cur - 1] = dist[cur] + 1

            dq.append(cur - 1)

        

        # 걷기 (+1)

        if 0 <= cur + 1 <= MAX and dist[cur + 1] == -1:

            dist[cur + 1] = dist[cur] + 1

            dq.append(cur + 1)

# 실행

N, K = map(int, input().split())

print(hide_and_seek(N, K))