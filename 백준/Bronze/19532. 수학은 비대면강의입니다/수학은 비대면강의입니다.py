# 입력 받기
a, b, c, d, e, f = map(int, input().split())

# 첫 번째 방정식에서 x를 구하기
x = (c * e - b * f) / (a * e - b * d)

# 두 번째 방정식에서 y를 구하기
y = (c * d - a * f) / (b * d - a * e)

# 결과 출력
print(int(x), int(y))


