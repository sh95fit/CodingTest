import re

def solution(myStr):
    answer = []
    answer = re.split('a|b|c', myStr)
    answer = [x for x in answer if x]
    if not len(answer) :
        answer.append("EMPTY")
    return answer