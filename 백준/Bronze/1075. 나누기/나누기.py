def find_min_suffix(N, F):

    base_number = (N // 100) * 100  # N의 마지막 두 자리를 00으로 바꾼 수

    for i in range(100):

        if (base_number + i) % F == 0:

            return f"{i:02d}"  # 두 자리 형식으로 반환

# 입력 받기

N = int(input().strip())

F = int(input().strip())

# 결과 계산

result = find_min_suffix(N, F)

# 결과 출력

print(result)

