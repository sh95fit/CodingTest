def solution(my_strings, parts):
    answer = ''
    for i, s in enumerate(my_strings) :
        answer += s[parts[i][0]:parts[i][1]+1]
    return(answer)