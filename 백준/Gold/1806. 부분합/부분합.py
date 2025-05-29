import sys

def min_subarray_length(N, S, arr):
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')

    while True:
        if current_sum >= S:
            min_length = min(min_length, end - start)
            current_sum -= arr[start]
            start += 1

        elif end == N:
            break

        else:
            current_sum += arr[end]
            end += 1

    return min_length if min_length != float('inf') else 0

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

print(min_subarray_length(N, S, arr))