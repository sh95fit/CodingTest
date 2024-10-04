import heapq
import sys

input = sys.stdin.read

def min_comparisons():
    data = input().split()
    N = int(data[0])
    card_sizes = list(map(int, data[1:N + 1]))

    if N == 1:
        print(0)

        return
   
    heapq.heapify(card_sizes)
    total_comparisons = 0
   
    while len(card_sizes) > 1:       
        first = heapq.heappop(card_sizes)
        second = heapq.heappop(card_sizes)
               
        comparisons = first + second
        total_comparisons += comparisons
              
        heapq.heappush(card_sizes, comparisons)

    print(total_comparisons)

if __name__ == "__main__":
    min_comparisons()

