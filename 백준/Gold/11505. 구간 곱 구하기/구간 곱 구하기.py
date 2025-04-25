import sys

input = sys.stdin.read

sys.setrecursionlimit(10**6)

MOD = 1_000_000_007

def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start] % MOD

    else:
        mid = (start + end) // 2
        build(arr, tree, node*2, start, mid)
        build(arr, tree, node*2+1, mid+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1]) % MOD

def update(tree, node, start, end, idx, val):
    if start == end:
        tree[node] = val % MOD

    else:
        mid = (start + end) // 2

        if start <= idx <= mid:
            update(tree, node*2, start, mid, idx, val)

        else:
            update(tree, node*2+1, mid+1, end, idx, val)

        tree[node] = (tree[node*2] * tree[node*2+1]) % MOD

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    l = query(tree, node*2, start, mid, left, right)
    r = query(tree, node*2+1, mid+1, end, left, right)

    return (l * r) % MOD

def main():
    data = input().split()
    idx = 0

    N, M, K = map(int, data[idx:idx+3])
    idx += 3
        
    arr = [0] + list(map(int, data[idx:idx+N]))  # 1-based index
    idx += N
    
    tree = [1] * (4 * N)
    build(arr, tree, 1, 1, N)
    result = []

    for _ in range(M + K):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])

        idx += 3

        if a == 1:
            update(tree, 1, 1, N, b, c)

        elif a == 2:
            res = query(tree, 1, 1, N, b, c)
            result.append(str(res))

    print('\n'.join(result))

if __name__ == "__main__":
    main()

