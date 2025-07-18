import sys
import heapq

input = sys.stdin.read

data = input().split()
index = 0
T = int(data[index])

index += 1
results = []

for _ in range(T):
    K = int(data[index])
    index += 1

    files = list(map(int, data[index:index + K]))
    index += K
    heapq.heapify(files)
    total_cost = 0

    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        cost = first + second
        total_cost += cost
        heapq.heappush(files, cost)

    results.append(str(total_cost))

print("\n".join(results))