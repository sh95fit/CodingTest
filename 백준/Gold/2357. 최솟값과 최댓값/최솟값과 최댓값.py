import sys

input = sys.stdin.read

class SegmentTree:
    def __init__(self, data, func, default):
        self.n = len(data)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
       
        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        res = self.default

        while l <= r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1

            if r % 2 == 0:
                res = self.func(res, self.tree[r])
                r -= 1

            l //= 2
            r //= 2

        return res

data = input().splitlines()
N, M = map(int, data[0].split())
arr = list(map(int, data[1:N+1]))
queries = [tuple(map(int, line.split())) for line in data[N+1:]]

min_tree = SegmentTree(arr, min, float('inf'))
max_tree = SegmentTree(arr, max, -float('inf'))

result = []

for a, b in queries:   
    min_value = min_tree.query(a-1, b-1)
    max_value = max_tree.query(a-1, b-1)

    result.append(f"{min_value} {max_value}")

sys.stdout.write("\n".join(result) + "\n")

