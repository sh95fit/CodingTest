def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for i, s in enumerate(my_string) :
        if i not in indices :
            answer += s
    return answer