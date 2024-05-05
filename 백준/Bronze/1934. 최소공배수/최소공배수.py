import math

# 최소공배수를 계산하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # A와 B 입력
    A, B = map(int, input().split())
    # 최소공배수 계산하여 출력
    print(lcm(A, B))
