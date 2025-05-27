from collections import defaultdict

def count_subarrays_with_sum_k(N, K, A):
    count = 0
    prefix_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  

    for num in A:
        prefix_sum += num
        count += prefix_counts[prefix_sum - K]
        prefix_counts[prefix_sum] += 1

    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(count_subarrays_with_sum_k(N, K, A))
