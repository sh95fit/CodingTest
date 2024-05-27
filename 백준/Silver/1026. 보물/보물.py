def minimize_S(N, A, B):

    # 배열 A를 오름차순으로 정렬

    A.sort()

    # 배열 B를 내림차순으로 정렬

    B.sort(reverse=True)

    

    # 최솟값을 계산

    S = 0

    for i in range(N):

        S += A[i] * B[i]

    

    return S

# 입력 받기

import sys

input = sys.stdin.read

data = input().split()

# 첫 번째 줄의 N을 파싱

N = int(data[0])

# 두 번째 줄의 A 배열을 파싱

A = list(map(int, data[1:N+1]))

# 세 번째 줄의 B 배열을 파싱

B = list(map(int, data[N+1:]))

# 결과 계산

result = minimize_S(N, A, B)

# 결과 출력

print(result)

