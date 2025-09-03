from collections import deque

import sys

input = sys.stdin.readline

def solve():

    data = input().split()

    if not data:

        return

    N = int(data[0])

    M = int(data[1])

    coins = []

    if N > 0:

        coins = list(map(int, input().split()))

    else:

        # N == 0 : 둘째 줄 없음

        coins = []

    # N == 0 처리

    if N == 0:

        print(0 if M == 0 else -1)

        return

    # 모든 동전이 0인 경우

    if all(p == 0 for p in coins):

        print(0 if M == 0 else -1)

        return

    # 0인 동전은 무의미(합을 바꾸지 않음) -> M==0일 때만 0 동전이 최소(0개)임

    # 따라서 BFS에는 0이 아닌 동전만 사용

    moves = [p for p in coins if p != 0]

    if not moves:

        # 모든 동전이 0이고 이미 위에서 처리했으므로 여기엔 올 수 없음

        print(-1)

        return

    # 빠른 특수검사: 동전이 하나뿐일 때 (대수적으로 검사)

    if len(moves) == 1:

        p = moves[0]

        # p * k = M, k >= 0 정수

        if p == 0:

            print(0 if M == 0 else -1)

            return

        # k must be integer >=0

        if M % p == 0:

            k = M // p

            if k >= 0:

                print(k)

                return

        print(-1)

        return

    # len(moves) == 2: BFS (일반적으로도 작동)

    LIMIT = 1_000_000  # 안전한 탐색 한계

    a, b = moves[0], moves[1]

    # BFS

    dq = deque()

    dq.append((0, 0))  # (sum, steps)

    visited = set()

    visited.add(0)

    if 0 == M:

        print(0)

        return

    while dq:

        s, steps = dq.popleft()

        for p in (a, b):

            ns = s + p

            if ns == M:

                print(steps + 1)

                return

            if -LIMIT <= ns <= LIMIT and ns not in visited:

                visited.add(ns)

                dq.append((ns, steps + 1))

    # 못찾음

    print(-1)

if __name__ == "__main__":

    solve()