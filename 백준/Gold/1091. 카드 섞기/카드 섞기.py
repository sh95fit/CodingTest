from collections import deque

def find_min_shuffle_count(N, P, S):
    initial_order = list(range(N))
    target_order = [i % 3 for i in range(N)]

    queue = deque([(initial_order, 0)])
    visited = set()
    visited.add(tuple(initial_order))

    while queue:
        current_order, shuffle_count = queue.popleft()

        if [P[current_order[i]] for i in range(N)] == target_order:
            return shuffle_count
        
        next_order = [0] * N

        for i in range(N):
            next_order[S[i]] = current_order[i]

        next_order_tuple = tuple(next_order)

        if next_order_tuple not in visited:
            visited.add(next_order_tuple)
            queue.append((next_order, shuffle_count + 1))

    return -1

N = int(input().strip())
P = list(map(int, input().strip().split()))
S = list(map(int, input().strip().split()))

print(find_min_shuffle_count(N, P, S))

