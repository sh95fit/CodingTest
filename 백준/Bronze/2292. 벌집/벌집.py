def min_rooms_to_pass(n):
    if n == 1:
        return 1
    
    # 1부터 시작하여 1씩 증가하는 수열
    rooms_in_circle = 1
    # 방이 1부터 시작하므로 원의 개수는 1부터 시작
    circles = 1
    
    # 원의 개수 구하기
    while rooms_in_circle < n:
        rooms_in_circle += 6 * circles
        circles += 1
    
    # 해당 원에서 목표 방까지의 거리 구하기
    distance_to_target = n - ((circles - 1) * (circles - 2) * 3) // 2
    
    return circles

def main():
    n = int(input().strip())
    print(min_rooms_to_pass(n))

if __name__ == "__main__":
    main()
