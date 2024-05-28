def create_sequence(length):

    sequence = []

    number = 1

    while len(sequence) < length:

        sequence.extend([number] * number)

        number += 1

    return sequence

def sum_of_sequence(A, B):

    sequence = create_sequence(B)

    return sum(sequence[A-1:B])

# 입력 받기

A, B = map(int, input().split())

# 결과 계산

result = sum_of_sequence(A, B)

# 결과 출력

print(result)

