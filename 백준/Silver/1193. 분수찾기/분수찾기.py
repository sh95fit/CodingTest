def find_fraction(x):
    diagonal_number = 1
    while x > diagonal_number:
        x -= diagonal_number
        diagonal_number += 1

    if diagonal_number % 2 == 0:
        numerator = x
        denominator = diagonal_number - x + 1
    else:
        numerator = diagonal_number - x + 1
        denominator = x

    return f"{numerator}/{denominator}"


# 입력 받기
x = int(input().strip())

# 분수 찾기 및 출력
print(find_fraction(x))
