def solution(my_string):
    answer = []
    for i in range(len(my_string)) :
        if my_string[i].isupper() :
            answer.append(my_string[i].lower())
        else :
            answer.append(my_string[i].upper())
    answer = ''.join(answer)
    return answer