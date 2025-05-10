import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    arr = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] = int(data[idx])
            idx += 1

    prefix = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix[i][j] = arr[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

    K = int(data[idx])
    idx += 1
    results = []
    for _ in range(K):
        i = int(data[idx])
        idx += 1
        j = int(data[idx])
        idx += 1
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1

        result = prefix[x][y] - prefix[i - 1][y] - prefix[x][j - 1] + prefix[i - 1][j - 1]
        results.append(str(result))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
