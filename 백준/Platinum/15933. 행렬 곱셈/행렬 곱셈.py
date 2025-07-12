import sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)

n = int(input())

MAX = 1001  # 차원 최대값 1000

# Disjoint Set (Union-Find)

parent = list(range(MAX))

def find(x):

    while parent[x] != x:

        parent[x] = parent[parent[x]]

        x = parent[x]

    return x

def union(x, y):

    x, y = find(x), find(y)

    if x != y:

        parent[y] = x

outdeg = [0] * MAX

indeg = [0] * MAX

deg = [0] * MAX  # 등장 여부 (outdeg + indeg > 0)

active_set = set()  # 등장한 차원들

# 결과 저장 리스트

result = []

plus_cnt = minus_cnt = big_diff = 0  # Δ=+1, Δ=−1, Δ의 절댓값이 2 이상

delta = [0] * MAX

for _ in range(n):

    r, c = map(int, input().split())

    # union-find 연결

    union(r, c)

    # 기존 delta 갱신

    for x, sign in [(r, +1), (c, -1)]:

        prev = delta[x]

        if abs(prev) > 1: big_diff -= 1

        elif prev == 1: plus_cnt -= 1

        elif prev == -1: minus_cnt -= 1

        delta[x] += sign

        now = delta[x]

        if abs(now) > 1: big_diff += 1

        elif now == 1: plus_cnt += 1

        elif now == -1: minus_cnt += 1

    # 등장 차원 처리

    for x in [r, c]:

        if deg[x] == 0:

            active_set.add(x)

        deg[x] += 1

    # 조건 확인

    if big_diff > 0 or plus_cnt > 1 or minus_cnt > 1 or plus_cnt != minus_cnt:

        result.append(0)

        continue

    # 연결 컴포넌트 확인

    roots = {find(x) for x in active_set}

    if len(roots) > 1:

        result.append(0)

        continue

    # 가능할 때 최대 면적 계산

    if plus_cnt == 0:

        # 오일러 회로: v x v 최대

        vmax = max(active_set)

        result.append(vmax * vmax)

    else:

        # 오일러 경로: start x end

        for i in active_set:

            if delta[i] == 1:

                s = i

            elif delta[i] == -1:

                t = i

        result.append(s * t)

# 출력

print("\n".join(map(str, result)))