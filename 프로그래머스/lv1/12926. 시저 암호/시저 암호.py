def solution(s, n):
    k = list(s)
    answer = []
    for i in k :
        if i == ' ' :
            answer.append(' ')
        else :
            if ord(i) <= 90 and ord(i)+n > 90 :
                answer.append(chr(ord(i)+n-26))
            elif ord(i)+n > 122 :
                answer.append(chr(ord(i)+n-26))
            else :
                answer.append(chr(ord(i)+n))
    answer = ''.join(answer)
    return answer