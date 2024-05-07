import math

def gcd(a, b):

    return math.gcd(a, b)

def lcm(a, b):

    return a * b // gcd(a, b)

# 입력 받기

a, b = map(int, input().split())

# 최소공배수 출력

print(lcm(a, b))

