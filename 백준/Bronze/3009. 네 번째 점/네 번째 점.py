# 입력 받기
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

# 같은 x좌표를 가진 두 점 찾기
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# x좌표 중복 찾기
for x in x_coords:
    if x_coords.count(x) == 1:
        x1 = x
        break

# y좌표 중복 찾기
for y in y_coords:
    if y_coords.count(y) == 1:
        y1 = y
        break

print(x1, y1)