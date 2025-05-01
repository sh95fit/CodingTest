import sys
input = sys.stdin.read

sys.setrecursionlimit(200000)

def solve():
    data = input().split()

    idx = 0
    N = int(data[idx]); idx += 1
    A = list(map(int, data[idx:idx+N]))

    idx += N
    M = int(data[idx]); idx += 1
    queries = data[idx:]    
    size = 1

    while size < N:
        size *= 2

    seg = [(float('inf'), -1)] * (2 * size)

    def build():
        for i in range(N):
            seg[size + i] = (A[i], i)

        for i in range(size - 1, 0, -1):
            seg[i] = min(seg[i * 2], seg[i * 2 + 1])

    def update(i, value):
        i += size
        seg[i] = (value, i - size)

        while i > 1:
            i //= 2
            seg[i] = min(seg[i * 2], seg[i * 2 + 1])

    def query(l, r):
        l += size
        r += size + 1
        res = (float('inf'), -1)

        while l < r:
            if l % 2 == 1:
                res = min(res, seg[l])
                l += 1

            if r % 2 == 1:
                r -= 1
                res = min(res, seg[r])

            l //= 2
            r //= 2

        return res[1] + 1  

    build()

    output = []
    q_idx = 0

    for _ in range(M):
        t = queries[q_idx]; q_idx += 1

        if t == '1':
            i = int(queries[q_idx]) - 1; q_idx += 1
            v = int(queries[q_idx]); q_idx += 1

            update(i, v)

        else: 
            i = int(queries[q_idx]) - 1; q_idx += 1
            j = int(queries[q_idx]) - 1; q_idx += 1

            output.append(str(query(i, j)))

    print("\n".join(output))

solve()