def solution(my_string, m, c):
    answer = ''
    answer += my_string[c-1::m]
    print(answer)
    return answer