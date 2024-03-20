# 과목별 등급에 따른 과목평점 매핑
grade_points = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

# 입력 받기
num_courses = 20  # 과목 수
total_credit = 0  # 총 학점
total_grade_point = 0  # 총 과목평점

for _ in range(num_courses):
    course_info = input().split()  # 과목명, 학점, 등급 입력 받기
    course_name = course_info[0]
    credit = float(course_info[1])
    grade = course_info[2]

    # 등급이 P가 아닌 경우에만 계산에 포함
    if grade != "P":
        total_credit += credit
        total_grade_point += credit * grade_points[grade]

# 전공평점 계산
if total_credit == 0:
    print("0.000000")  # 학점이 0인 경우
else:
    gpa = total_grade_point / total_credit
    print(f"{gpa:.6f}")