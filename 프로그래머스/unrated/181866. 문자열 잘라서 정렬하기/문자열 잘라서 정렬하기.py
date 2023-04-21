def solution(myString):
    answer = myString.split('x')
    answer = [i for i in answer if i]
    return sorted(answer)