def solution(age):
    answer = ''
    for i in range(len(str(age))) :
        answer += chr(97+int(str(age)[i]))
    return answer