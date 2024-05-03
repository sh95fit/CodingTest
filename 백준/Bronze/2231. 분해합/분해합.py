def calculate_decomposition(n):
    # 분해합을 계산하는 함수
    return n + sum(int(digit) for digit in str(n))

def find_smallest_constructor(N):
    # 가장 작은 생성자를 찾는 함수
    for i in range(1, N+1):
        if calculate_decomposition(i) == N:
            return i
    return 0

# 입력 받기
N = int(input())

# 결과 출력
print(find_smallest_constructor(N))

