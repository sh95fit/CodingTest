import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    row = list(map(int, input().split()))
    for num in row:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])

