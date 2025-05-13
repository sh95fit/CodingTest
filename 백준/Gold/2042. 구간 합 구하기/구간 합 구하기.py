import sys

input = sys.stdin.readline

def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(arr, tree, node*2, start, mid) + init(arr, tree, node*2+1, mid+1, end)

    return tree[node]

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2

    return query(tree, node*2, start, mid, left, right) + query(tree, node*2+1, mid+1, end, left, right)

def update(arr, tree, node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(arr, tree, node*2, start, mid, index, diff)
        update(arr, tree, node*2+1, mid+1, end, index, diff)

N, M, K = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]  
tree = [0] * (4 * N)
init(arr, tree, 1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(arr, tree, 1, 1, N, b, diff)

    elif a == 2:
        print(query(tree, 1, 1, N, b, c))