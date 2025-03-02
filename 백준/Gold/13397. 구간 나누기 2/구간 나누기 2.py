def can_divide(arr, N, M, max_diff):   
    current_max = arr[0]
    current_min = arr[0]
    count = 1  

    for i in range(1, N):
        current_max = max(current_max, arr[i])
        current_min = min(current_min, arr[i])

        if current_max - current_min > max_diff:            
            count += 1
            current_max = arr[i]
            current_min = arr[i]

            if count > M:  
                return False

    return True

def solve(N, M, arr): 
    left, right = 0, max(arr) - min(arr)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if can_divide(arr, N, M, mid):
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer

N, M = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(N, M, arr))

