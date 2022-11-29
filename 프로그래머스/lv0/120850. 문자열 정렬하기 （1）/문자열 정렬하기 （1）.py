def solution(my_string):
    ''' 
    answer = []
    for i in range(len(my_string)) :
        if my_string[i].isdigit() :
            answer.append(int(my_string[i]))
    answer.sort()
    return answer
    '''
    answer = sorted(map(int, filter(lambda x : x.isdigit(), my_string)))
    return answer