import sys
import heapq

def solve_problem_order(n, m, prerequisites):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for a, b in prerequisites:
        graph[a].append(b)
        indegree[b] += 1

    heap = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    result = []
    while heap:
        current = heapq.heappop(heap)
        result.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    prerequisites = [(int(data[i]), int(data[i+1])) for i in range(2, len(data), 2)]

    order = solve_problem_order(n, m, prerequisites)
    print(' '.join(map(str, order)))
