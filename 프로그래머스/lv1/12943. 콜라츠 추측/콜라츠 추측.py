def solution(num):
    cnt = 0
    if num == 1 :
        answer = 0;
    else : 
        while True : 
            if num == 1 :
                answer = cnt
                break
            elif cnt > 500 :
                answer = -1
                break
            else :
                if num%2 == 0 : 
                    num = num/2
                else :
                    num = num*3 + 1
            cnt += 1
    return answer