def solution(my_string):
    answer = []
    for i in range(26) :
        answer.append(my_string.count(f'{chr(65+i)}'))
    for i in range(26) :
        answer.append(my_string.count(f'{chr(97+i)}'))
    return answer