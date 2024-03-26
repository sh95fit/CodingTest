# 색종이의 수
N = int(input())

# 색종이가 붙은 위치를 저장할 2차원 배열 초기화
paper = [[0] * 100 for _ in range(100)]

# 각 색종이의 위치에 1을 표시
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 검은 영역의 넓이 계산
black_area = 0
for i in range(100):
    for j in range(100):
        black_area += paper[i][j]

# 결과 출력
print(black_area)
