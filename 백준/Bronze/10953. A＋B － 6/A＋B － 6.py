T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):

    line = input()

    A, B = map(int, line.split(','))

    print(A + B)