while True:
    try:
        # 한 줄씩 입력 받기
        line = input()
        
        # 입력이 없을 경우 종료
        if not line:
            break
        
        # 입력을 그대로 출력
        print(line)

    except EOFError:
        break