from collections import deque

def flip(arr, start, K):
    arr = list(arr)
    arr[start:start+K] = reversed(arr[start:start+K])

    return tuple(arr)

def min_flips_to_sort(N, K, permutation):
    target = tuple(sorted(permutation))
    initial_state = tuple(permutation)
    
    if initial_state == target:
        return 0
    
    queue = deque([(initial_state, 0)])  
    visited = set()
    visited.add(initial_state)

    while queue:
        current, moves = queue.popleft()
        
        for i in range(N - K + 1):
            next_permutation = flip(current, i, K)

            if next_permutation == target:
                return moves + 1

            if next_permutation not in visited:
                visited.add(next_permutation)
                queue.append((next_permutation, moves + 1))

    return -1

N, K = map(int, input().split())
permutation = list(map(int, input().split()))

result = min_flips_to_sort(N, K, permutation)
print(result)

