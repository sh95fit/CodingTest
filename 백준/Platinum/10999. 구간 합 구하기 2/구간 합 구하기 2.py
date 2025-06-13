import sys
input = sys.stdin.read
sys.setrecursionlimit(2 * 10**6)

data = input().split()
n, m, k = map(int, data[:3])
nums = list(map(int, data[3:3+n]))
queries = data[3+n:]

size = 1
while size < n:
    size *= 2

tree = [0] * (2 * size)
lazy = [0] * (2 * size)

def build():
    for i in range(n):
        tree[size + i] = nums[i]
    for i in range(size - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

def propagate(node, node_left, node_right):
    if lazy[node] != 0:
        tree[node] += lazy[node] * (node_right - node_left + 1)
        if node < size:  
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0

def update(left, right, diff, node=1, node_left=0, node_right=size-1):
    propagate(node, node_left, node_right)
    if right < node_left or node_right < left:
        return
    if left <= node_left and node_right <= right:
        lazy[node] += diff
        propagate(node, node_left, node_right)
        return
    mid = (node_left + node_right) // 2
    update(left, right, diff, node*2, node_left, mid)
    update(left, right, diff, node*2+1, mid+1, node_right)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(left, right, node=1, node_left=0, node_right=size-1):
    propagate(node, node_left, node_right)
    if right < node_left or node_right < left:
        return 0
    if left <= node_left and node_right <= right:
        return tree[node]
    mid = (node_left + node_right) // 2
    return query(left, right, node*2, node_left, mid) + query(left, right, node*2+1, mid+1, node_right)

build()

output = []
i = 0
while i < len(queries):
    a = int(queries[i])
    b = int(queries[i+1]) - 1
    c = int(queries[i+2]) - 1
    if a == 1:
        d = int(queries[i+3])
        update(b, c, d)
        i += 4
    elif a == 2:
        result = query(b, c)
        output.append(str(result))
        i += 3

print('\n'.join(output))
