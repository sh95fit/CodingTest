def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    arr = list(map(int, data[2:N+2]))
    queries = []
    
    index = N + 2
    for _ in range(M):
        i = int(data[index])
        j = int(data[index + 1])
        queries.append((i, j))
        index += 2
    
    results = range_sum(N, M, arr, queries)
    for result in results:
        print(result)

def range_sum(N, M, arr, queries):
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    results = []
    for query in queries:
        i, j = query
        sum_range = prefix_sum[j] - prefix_sum[i - 1]
        results.append(sum_range)
    
    return results

if __name__ == "__main__":
    main()
