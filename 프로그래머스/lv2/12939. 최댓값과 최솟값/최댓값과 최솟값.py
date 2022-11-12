import re
def solution(s):
    answer = []
#    k = []
    s = re.findall("-?\d+", s)
    k = list(map(int, s))
#   k = [int(i) for i in s]
#    for i in s :
#        k.append(int(i))
    answer.append(min(k))
    answer.append(max(k))
    answer = ' '.join(map(str, answer))
    return answer