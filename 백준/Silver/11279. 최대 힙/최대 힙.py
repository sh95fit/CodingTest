import sys

import heapq

input = sys.stdin.read

def main():
    data = input().splitlines()
    N = int(data[0])  
    max_heap = []
    result = []
    
    for i in range(1, N + 1):
        x = int(data[i])
        
        if x == 0:
            if max_heap:              
                result.append(-heapq.heappop(max_heap))
            else:
                result.append(0)

        else:           
            heapq.heappush(max_heap, -x)
       
    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()

