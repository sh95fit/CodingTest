from collections import deque

def min_operations_to_remove(N, M, positions):

    # 초기 큐 상태를 생성

    queue = deque(range(1, N + 1))

    total_operations = 0

    for position in positions:

        # 뽑아내려는 위치의 원소가 현재 큐의 어느 위치에 있는지 찾음

        idx = queue.index(position)

        # 왼쪽으로 이동하는 거리

        left_distance = idx

        # 오른쪽으로 이동하는 거리

        right_distance = len(queue) - idx

        

        # 최소 이동 거리 선택

        if left_distance <= right_distance:

            total_operations += left_distance

            queue.rotate(-left_distance)

        else:

            total_operations += right_distance

            queue.rotate(right_distance)

        

        # 첫 번째 원소를 제거 (뽑아냄)

        queue.popleft()

    

    return total_operations

# 입력 받기

N, M = map(int, input().split())

positions = list(map(int, input().split()))

# 결과 출력

print(min_operations_to_remove(N, M, positions))

