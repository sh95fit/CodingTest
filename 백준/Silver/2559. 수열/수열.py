import sys

def max_temperature_sum(N, K, temps):

    # 초기 K일의 합 계산

    current_sum = sum(temps[:K])

    max_sum = current_sum

    # 슬라이딩 윈도우 적용

    for i in range(K, N):

        current_sum = current_sum - temps[i - K] + temps[i]

        max_sum = max(max_sum, current_sum)

    return max_sum

# 입력 처리

N, K = map(int, input().split())

temps = list(map(int, input().split()))

# 결과 출력

print(max_temperature_sum(N, K, temps))