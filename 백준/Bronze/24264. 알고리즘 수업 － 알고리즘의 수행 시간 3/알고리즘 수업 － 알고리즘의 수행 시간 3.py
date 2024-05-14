def main():
    n = int(input())

    # 이중 반복문으로 인해 발생하는 곱셈 횟수 계산
    multiplications = n * n

    # 곱셈 횟수를 다항식으로 표현했을 때 최고차항의 차수 구하기
    degree = min(2, n * 2)

    print(multiplications)  # 곱셈 횟수 출력
    print(degree)  # 최고차항의 차수 출력

if __name__ == "__main__":
    main()


