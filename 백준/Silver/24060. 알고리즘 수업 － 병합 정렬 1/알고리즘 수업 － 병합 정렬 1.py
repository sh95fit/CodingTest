import sys
sys.setrecursionlimit(10**6)

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, result
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    for i in range(len(tmp)):
        A[p + i] = tmp[i]
        count += 1
        if count == K:
            result = tmp[i]

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
result = -1

merge_sort(A, 0, N - 1)
print(result)
