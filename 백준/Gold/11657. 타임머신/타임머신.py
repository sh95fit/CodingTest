import sys

input = sys.stdin.readline

INF = int(1e9)

def bellman_ford(n, edges, start):

    dist = [INF] * (n + 1)

    dist[start] = 0

    # N-1번 반복

    for i in range(n - 1):

        for a, b, c in edges:

            if dist[a] != INF and dist[b] > dist[a] + c:

                dist[b] = dist[a] + c

    # N번째에서 갱신 → 음수 사이클 존재

    for a, b, c in edges:

        if dist[a] != INF and dist[b] > dist[a] + c:

            return None  # 음수 사이클 발견

    

    return dist

def main():

    n, m = map(int, input().split())

    edges = []

    for _ in range(m):

        a, b, c = map(int, input().split())

        edges.append((a, b, c))

    result = bellman_ford(n, edges, 1)

    if result is None:  # 음수 사이클

        print(-1)

    else:

        for i in range(2, n + 1):

            if result[i] == INF:

                print(-1)

            else:

                print(result[i])

if __name__ == "__main__":

    main()