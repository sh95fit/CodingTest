def count_less_equal(mid, n):
    count = 0

    for i in range(1, n + 1):
        count += min(mid // i, n)

    return count

def find_kth_number(n, k):
    low, high = 1, n * n   

    while low < high:
        mid = (low + high) // 2

        if count_less_equal(mid, n) < k:
            low = mid + 1

        else:
            high = mid

    return low

n = int(input())
k = int(input())

print(find_kth_number(n, k))

