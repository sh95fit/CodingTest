def solution(my_str, n):
    answer = []
    cnt = 0
    cnt_n = 1
    if len(my_str)%n == 0 :
        for i in range(len(my_str)//n) :
            answer.append(my_str[cnt:n*cnt_n])
            cnt = n*cnt_n
            cnt_n += 1
    else :
        for i in range(len(my_str)//n+1) :
            answer.append(my_str[cnt:n*cnt_n])
            cnt = n*cnt_n
            cnt_n += 1
            
    return answer