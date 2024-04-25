# 세 각의 크기를 입력 받음
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# 세 각의 합을 계산
angle_sum = angle1 + angle2 + angle3

# 세 각의 크기가 모두 60이면 Equilateral
if angle1 == angle2 == angle3 == 60:
    print("Equilateral")
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
elif angle_sum == 180 and (angle1 == angle2 or angle2 == angle3 or angle1 == angle3):
    print("Isosceles")
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
elif angle_sum == 180:
    print("Scalene")
# 세 각의 합이 180이 아닌 경우에는 Error
else:
    print("Error")
